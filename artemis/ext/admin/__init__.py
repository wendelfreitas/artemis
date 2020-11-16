from flask_admin import Admin
from flask_admin.actions import action
from flask_admin.contrib.sqla import ModelView, filters
from artemis.ext.db import db
from artemis.ext.db.models import User
from flask import flash

from flask_simplelogin import SimpleLogin, login_required
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla

from flask import request, render_template
from flask import Blueprint

site_admin = Admin()

def verify_login(user):
    if (user.get("username") == "admin" and user.get("password") == "123!"):
        return True
    else:
        return False

AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)

def format_user(self, request, user, *args):
    return user.email.split("@")[0]


class UserAdmin(ModelView):
    column_formatters = {"email": format_user}
    column_list = ["email", "admin"]
    column_searchable_list = ["email"]
    
    column_filters = [
        "email",
        "admin",
        filters.FilterLike(
            User.email,
            "Dominio",
            options=(('gmail', 'Gmail'), ('ite', 'ITE'))
        )
    ]
    
    can_edit = False
    can_create = True
    can_delete = True
    
    @action(
        "Toggle_admin",
        "Toggle admin status",
        "Você tem certeza?"
    )
    def toggle_admin_status(self, ids):
        for user in User.query.filter(User.id.in_(ids)).all():
            user.admin = not user.admin
        db.session.commit()
        flash("Alteração realizada com sucesso!", "success")

def init_app(app):
    site_admin.init_app(app)
    site_admin.name = app.config["ADMIN_NAME"]
    site_admin.template_mode = "bootstrap3"
    
    site_admin.add_view(UserAdmin(User, db.session))
    
    SimpleLogin(app, login_checker=verify_login)
    