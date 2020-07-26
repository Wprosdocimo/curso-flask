from flask import Blueprint, render_template, current_app


bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    site_name = "Eita Loco"
    current_app.logger.debug("Entrei na função main")
    return render_template("index.html", site_name=site_name)

@bp.route("/sobre")
def about():
    return render_template("about.html")

@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")