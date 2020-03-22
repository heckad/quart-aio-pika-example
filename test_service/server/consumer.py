import asyncio

import aio_pika
from aio_pika.patterns import RPC

from server.app import app as application

application.logger.info('Started')


async def multiply(*, x, y):
    application.logger.info('multiply')
    return x * y


async def main():
    connection = await connect_robust(
        application.config['AMPQ_URL'],
        client_properties={'connection_name': 'callee'}
    )

    # Creating channel
    channel = await connection.channel()

    rpc = await RPC.create(channel)
    await rpc.register('multiply', multiply, auto_delete=True)

    return connection


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    connection = loop.run_until_complete(main())

    try:
        loop.run_forever()
    finally:
        loop.run_until_complete(connection.close())
        loop.shutdown_asyncgens()
