from flask_migrate import Migrate
from artemis.ext.db import db
from artemis.ext.db import models

migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)