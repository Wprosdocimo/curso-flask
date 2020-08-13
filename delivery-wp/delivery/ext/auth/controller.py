import os
from werkzeug.security import generate_password_hash, check_password_hash
from delivery.ext.auth.models import User
from delivery.ext.db import db
from werkzeug.utils import  secure_filename

from flask import current_app as app

ALG = "pbkdf2:sha256"

def create_user(
    email: str,
    password: str,
    admin: bool = False
    ) -> User:
    user = User(
        email=email,
        passwd = generate_password_hash(password, ALG),
        admin = admin
    )
    db.session.add(user)
    # TODO: Tratar exception caso user já exista
    db.session.commit()
    return user

def save_user_foto(filename, filestorage):
    """
    Saves user foto in
    ./uploads/foo/tstts.ext
    """
    filename = os.path.join(
        app.config["UPLOAD_FOLDER"],
        secure_filename(
            filename
        )
    )
    # TODO:
    # 1) verificar se o diretório existe
    # 2) Criar o diretorio
    filestorage.save(filename)