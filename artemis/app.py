from flask import Flask

from artemis.ext import site
from artemis.ext import db
from artemis.ext import config
from artemis.ext import cli
from artemis.ext import migrate
from artemis.ext import admin


def create_app():
    app = Flask(__name__)    
    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    admin.init_app(app)
    cli.init_app(app)
    site.init_app(app)
    return app
