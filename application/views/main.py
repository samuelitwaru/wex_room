from flask import Blueprint, request, render_template, redirect


main_bp = Blueprint('main_bp', __name__, url_prefix="/")


@main_bp.route("/")
def main():
    return render_template("main/main-menu.html")

