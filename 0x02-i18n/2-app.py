#!/usr/bin/env python3
"""1. Basic Babel setup
"""

from flask_babel import Babel
from flask import Flask, render_template, request


app = Flask(__name__)

babel = Babel(app)


class Config:
    """ a Config class that has a LANGUAGES"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ a single / route """
    return render_template('2-index.html')


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
