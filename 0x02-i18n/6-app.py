#!/usr/bin/env python3
"""Creating a user login system is outside the scope of this project
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, Locale
from typing import Optional

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    configuration class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_user(login_as):
    """user find"""
    try:
        return users.get(int(login_as))
    except Exception:
        return None


@app.before_request
def before_request():
    """before request"""
    g.user = get_user(request.args.get("login_as"))


@babel.localeselector
def get_locale():
    """get_locale"""
    locale = request.args.get('locale')
    if locale:
        return locale
    lang = request.args.get("login_as")
    if lang:
        lang = lang.get(int(lang)).get("locale")
        if lang in app.config['LANGUAGES']:
            return lang
    head = request.headers.get("locale")
    if head:
        return head
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def run():
    """return templates/6-index.html"""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
