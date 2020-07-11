from flask import render_template, current_app
from flask import Blueprint


bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    current_app.logger.debug("Entrei na função main")
    return render_template("index.html")

@bp.route("/sobre")
def about():
    return render_template("about.html")

@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")