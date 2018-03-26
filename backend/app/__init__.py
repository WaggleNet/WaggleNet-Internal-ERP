from flask import Flask
from .services.json_encode import AppJSONEncoder


def make_app():
    from .model import db
    from .config import Config
    from .services import bcrypt
    from .api import account, transaction, user
    app = Flask(__name__)
    app.json_encoder = AppJSONEncoder
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    # Register blueprints
    app.register_blueprint(account.blueprint)
    app.register_blueprint(user.blueprint)
    app.register_blueprint(transaction.blueprint)
    return app
