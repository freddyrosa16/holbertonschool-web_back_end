#!/usr/bin/env python3
"""
Welcome to Holberton
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class for setting available languages and default locale and timezone
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route("/", methods=['GET'])
def helloWorld():
    """
    Hello world
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
