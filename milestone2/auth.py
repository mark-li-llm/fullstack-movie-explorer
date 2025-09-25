from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    logout_user,
    login_required,
    current_user,
)
from models import db, User

auth_bp = Blueprint("auth_bp", __name__)

login_manager = LoginManager()
login_manager.login_view = "auth_bp.login"


class LoginUser(UserMixin):
    """
    A simple wrapper class that holds the User information from the database.
    Alternatively, you can have the User class in models.py inherit from UserMixin.
    """

    def __init__(self, user):
        self.id = user.id
        self.username = user.username


@login_manager.user_loader
def load_user(user_id):
    """Retrieve the user object from the database based on user_id."""
    user = User.query.get(int(user_id))
    if user:
        return LoginUser(user)
    return None


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            flash("Please enter a username", "error")
            return redirect(url_for("auth_bp.login"))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            login_user(LoginUser(existing_user))
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        else:
            flash("Username does not exist. Please sign up first.", "error")
            return redirect(url_for("auth_bp.login"))
    return render_template("login.html")


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        if not username:
            flash("Please enter a username", "error")
            return redirect(url_for("auth_bp.signup"))

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash(
                "Username already exists. Please log in directly or choose a different username.",
                "error",
            )
            return redirect(url_for("auth_bp.signup"))

        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration successful, please log in!", "success")
        return redirect(url_for("auth_bp.login"))
    return render_template("signup.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth_bp.login"))
