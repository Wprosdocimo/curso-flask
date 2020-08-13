from flask import Blueprint, render_template, current_app, redirect, request
from delivery.ext.auth.form import UserForm
from delivery.ext.auth.controller import create_user, save_user_foto

bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    site_name = "Eita Loco"
    current_app.logger.debug("Entrei na função main")
    return render_template("index.html", site_name=site_name)

@bp.route("/sobre")
def about():
    return render_template("about.html")


@bp.route("/cadastro", methods=["POST", "GET"])
def signup():
    form = UserForm()
    if form.validate_on_submit():
        create_user(
            email = form.email.data,
            password = form.password.data
        )
        foto = request.files.get('foto')
        if foto:
            save_user_foto(
                foto.filename,
                foto
            )
        # forçar login
        return redirect("/")
    
    # if request.method == "POST":
    #     __import__("ipdb").set_trace()


    return render_template("userform.html", form=form)


@bp.route("/restaurantes")
def restaurants():
    return render_template("restaurants.html")