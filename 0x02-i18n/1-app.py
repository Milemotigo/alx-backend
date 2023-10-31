#!/usr/bin/env python3
"""1. Basic Babel setup
"""

from flask_babel import Babel
from flask import Flask


app = Flask(__name__)

babel = Babel(app)


class Config:

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


if __name__ == "__main__":
    app.run()
