import asyncio

import hypercorn.asyncio
from hypercorn.config import Config
from quart import jsonify

from aio_pika import connect_robust
from aio_pika.patterns import RPC

from server.app import app as application

application.logger.info('Started')

config = Config()
config.bind = ['0.0.0.0:8000']
config.use_reloader = True

async def main():
    connection = await connect_robust(
        application.config['AMPQ_URL'],
        client_properties={'connection_name': 'caller'}
    )

    async with connection:
        channel = await connection.channel()
        rpc = await RPC.create(channel)
        result = await rpc.proxy.multiply(x=100, y=5)
        application.logger.info(result)

async def pub():
    await main()
    return jsonify({}), 200

# HTTP
application.add_url_rule('/api/pub', methods=['GET'], view_func=pub)

loop = asyncio.get_event_loop()
loop.run_until_complete(hypercorn.asyncio.serve(application, config))
