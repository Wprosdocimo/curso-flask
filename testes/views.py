from flask import Flask


def init_app(app: Flask):
    """Inicialização de extenções"""

    @app.route("/")
    def index():
        return "Hello World"

    @app.route("/contato")
    def contato():
        return "<form><input type='text'></input></form>"





