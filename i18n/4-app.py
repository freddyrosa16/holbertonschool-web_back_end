#!/usr/bin/env python3
"""
Welcome to Holberton
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


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


def get_locale():
    """
    Determine the best match with our supported languages.
    Check for locale parameter in request args.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route("/", methods=['GET'])
def helloWorld():
    """
    Hello world
    """
    return render_template('0-index.html', title=_("home_title"), header=_("home_header"))


if __name__ == '__main__':
    app.run(debug=True)
