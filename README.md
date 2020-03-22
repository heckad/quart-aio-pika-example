# README

1. Run `docker-compose up`
2. Make a request: `http://localhost:8001/api/pub`

It throws:

```
asgi_1      | [2020-03-22 14:36:40,469] ERROR in app: Exception on request GET /api/pub
asgi_1      | Traceback (most recent call last):
asgi_1      |   File "/usr/local/lib/python3.6/site-packages/quart/app.py", line 1451, in handle_request
asgi_1      |     return await self.full_dispatch_request(request_context)
asgi_1      |   File "/usr/local/lib/python3.6/site-packages/quart/app.py", line 1473, in full_dispatch_request
asgi_1      |     result = await self.handle_user_exception(error)
asgi_1      |   File "/usr/local/lib/python3.6/site-packages/quart/app.py", line 892, in handle_user_exception
asgi_1      |     raise error
asgi_1      |   File "/usr/local/lib/python3.6/site-packages/quart/app.py", line 1471, in full_dispatch_request
asgi_1      |     result = await self.dispatch_request(request_context)
asgi_1      |   File "/usr/local/lib/python3.6/site-packages/quart/app.py", line 1519, in dispatch_request
asgi_1      |     return await handler(**request_.view_args)
asgi_1      |   File "asgi.py", line 31, in pub
asgi_1      |     await main()
asgi_1      |   File "asgi.py", line 27, in main
asgi_1      |     result = await rpc.proxy.multiply(x=100, y=5)
asgi_1      |   File "/usr/local/lib/python3.6/site-packages/aio_pika/patterns/rpc.py", line 341, in call
asgi_1      |     return await future
asgi_1      | aiormq.exceptions.DeliveryError: (IncomingMessage:{'app_id': None,
asgi_1      |  'body_size': 28,
asgi_1      |  'cluster_id': '',
asgi_1      |  'consumer_tag': None,
asgi_1      |  'content_encoding': '',
asgi_1      |  'content_type': '',
asgi_1      |  'correlation_id': '140270532208232',
asgi_1      |  'delivery_mode': 1,
asgi_1      |  'delivery_tag': None,
asgi_1      |  'exchange': '',
asgi_1      |  'expiration': None,
asgi_1      |  'headers': {'From': b'amq_k5mnws4y5towgel4em2wcp4e4e'},
asgi_1      |  'message_id': '7fa596213ab34c0c27f0e762feb9bb47',
asgi_1      |  'priority': 5,
asgi_1      |  'redelivered': None,
asgi_1      |  'reply_to': 'amq_k5mnws4y5towgel4em2wcp4e4e',
asgi_1      |  'routing_key': 'multiply',
asgi_1      |  'timestamp': datetime.datetime(2020, 3, 22, 14, 36, 40),
asgi_1      |  'type': 'call',
asgi_1      |  'user_id': None}, None)
```
