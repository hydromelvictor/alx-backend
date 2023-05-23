#!/usr/bin/env python3
"""First you will setup a basic Flask app in 0-app.py
"""
from flask import Flask, render_template, request, localeselector
from flask_babel import Babel, Locale, timezone, _
from typing import Optional, Text

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    configuration class
    """
    LANGUAGES = ["en", "fr"]


babel.default_locale = Config.LANGUAGES[0]
babel.default_timezone = timezone('UTC')


@babel.localeselector
def get_locale():
    """get_locale"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route("/", strict_slashes=False)
def run() -> Text:
    """return templates/3-index.html"""
    return render_template("3-index.html", lang=babel.default_locale)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
