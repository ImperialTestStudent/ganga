"""Contains the configuration settings for the GUI Flask App"""

import os


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "f3aa26t8b537abf6ee6305eefea0a10a"
