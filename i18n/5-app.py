#!/usr/bin/env python3
"""
Welcome to Holberton
"""
from flask import Flask, render_template, request, g
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

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user():
    """
    Retrieve user by ID from URL parameter.
    Return None if the ID cannot be found or if login_as is not passed.
    """
    user_id = request.args.get('login_as')
    if user_id is not None:
        try:
            user_id = int(user_id)
            return users.get(user_id)
        except ValueError:
            return None
    return None


@app.before_request
def before_request():
    """
    Execute before each request to set the user in flask.g
    """
    g.user = get_user()


@app.route("/", methods=['GET'])
def helloWorld():
    """
    Hello world
    """
    if g.user:
        welcome_message = _("logged_in_as", username=g.user['name'])
    else:
        welcome_message = _("not_logged_in")
    return render_template('0-index.html', title=_("home_title"), header=_("home_header"), welcome_message=welcome_message)


if __name__ == '__main__':
    app.run(debug=True)
