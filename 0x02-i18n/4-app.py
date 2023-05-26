#!/usr/bin/env python3
"""First you will setup a basic Flask app in 0-app.py
"""
from flask import Flask, render_template, request
from flask_babel import Babel

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


# app.config.from_object(Config)
@babel.localeselector
def get_locale():
    """get_locale"""
    locale = request.args.get('locale')
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def run():
    """return templates/4-index.html"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
