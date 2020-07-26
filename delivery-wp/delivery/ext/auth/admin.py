from flask_admin.contrib.sqla import ModelView, filters
from flask_admin.actions import action
from delivery.ext.auth.models import User
from delivery.ext.db import db
from flask import flash, Markup

# def format_user(self, request, user, *args):
#     return user.email.split("@")[0]
    # return user.email.partition("@")[0]
    # return user.email.re.sub(r'([\w\.]+)(@.+\..{2,3})',"foo",email)


# TODO: descrever todos os models

class UserAdmin(ModelView):
    """Interface admin de users"""

    # column_formatters = {"email": format_user}
    column_formatters = {
        "email": lambda s, r, u, *a: Markup(f'<b>{u.email.split("@")[0]}</b>')
    }
    column_list = ["admin", "email"]
    column_searchable_list = ["email"]
    column_filters = [
        "email",
        "admin",
        filters.FilterLike(
            User.email,
            "dominio",
            options=(("gmail", "Gmail"), ("uol", "Uol"))
        )
    ]

    can_create = True
    can_delete = True
    can_edit = False

    @action(
        'toggle_admin',
        'Toggle Admin', 
        'Are you sure?'
    )
    def toggle_admin_status(self, ids):
        users = User.query.filter(User.id.in_(ids)).all()
        for user in users:
            user.admin = not user.admin
        db.session.commit()
        flash(f"{users.count()} Usuários alterados com sucesso!!", "success")
