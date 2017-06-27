import os
from ConfigParser import ConfigParser


def load_api_key(app_name):
    parser = ConfigParser()
    parser.read(os.path.normpath(os.path.expanduser("~/.keys.conf")))
    return parser.get(app_name, 'api_key')
