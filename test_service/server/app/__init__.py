from quart import Quart

__all__ = [
    'app'
]

app = Quart(__name__)
app.config.from_object('server.app.config.Development')
