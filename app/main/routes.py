from flask import render_template, redirect, url_for
from app import db
from app.models import DbGame, GameStatus
from app.main import bp


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/ajax")
def ajax():
    data = db.session.query(DbGame).order_by(DbGame.time.desc()).limit(10)
    return render_template("ajax.html", games=data, GameStatus=GameStatus)

