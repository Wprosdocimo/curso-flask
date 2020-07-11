from delivery.ext.db import db
# from delivery.ext.site import models
from flask import click


def init_app(app):
    @app.cli.command()
    def create_db():
        """Este comando inicializa o db"""
        db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_Flag=True, default=False)
    def add_user():
        """Adiciona novo usuário"""
        user = models.User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()

        click.echo(f"Usuário {email} criado com sucesso!")

    @app.cli.command()
    def listar_pedidos():
        return True