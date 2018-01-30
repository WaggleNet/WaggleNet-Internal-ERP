from flask import Flask


def make_app():
    from .model import db
    from .config import Config
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    return app
