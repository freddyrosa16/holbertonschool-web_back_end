
#!/usr/bin/env python3
"""
basic app
"""
import flask
from os import environ

app = flask.Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    return home template
    """
    return flask.render_template("0-index.html")


if __name__ == "__main__":
    app.run(
        environ.get("HOST"), environ.get("PORT")
    )
