import os

__all__ = [
    'Development'
]


class Development:
    DEBUG = True
    TESTING = True

    SECRET_KEY = b'\xce\x08\xa8y\x94\x1a|\x10\x06\xd4(\xc6A\x87\xe9mlm>\xe1p\xcfNd'

    AMPQ_URL = 'amqp://dev_user:0000@rabbit:5672/tgvhost'
