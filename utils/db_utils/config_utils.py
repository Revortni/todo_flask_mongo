import configparser
import os
import base64


def load_config(namespace):
    _CONFIG_FILE_PATH: str = 'config.ini'
    config = configparser.ConfigParser()
    if os.path.exists(_CONFIG_FILE_PATH):
        config.read(_CONFIG_FILE_PATH)
    else:
        print("Config.ini is missing")

    return config[namespace]


def b64_decode(encoded_text):
    return base64.b64decode(encoded_text).decode("utf-8")
