from flask import Flask
from app.models.book import db


def register_buleprint(app):
    from app.web.book import web
    app.register_blueprint(web)


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.secure")
    app.config.from_object("app.setting")
    register_buleprint(app=app)
    db.init_app(app)
    db.create_all(app=app)
    return app
