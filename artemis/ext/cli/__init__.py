import click
from artemis.ext.db import db
from artemis.ext.db import models


def init_app(app):
    
    @app.cli.command()
    def create_db():
        """ Comando que start o db """
        db.create_all()
        click.echo("DB criado com sucesso!")
        
    
    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """ Add usuario """
        user = models.User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()
        
        
    @app.cli.command()
    def list_users():
        """ Lista usuarios """
        user = models.User.query.all()
        click.echo(f"{user}")