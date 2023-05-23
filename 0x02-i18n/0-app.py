#!/usr/bin/env python3
"""First you will setup a basic Flask app in 0-app.py
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def run():
    """return templates/0-index.html"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
