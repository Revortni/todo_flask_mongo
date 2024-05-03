import snowflake.connector
import configparser
import os


def load_config(namespace):
    _CONFIG_FILE_PATH: str = 'config.ini'
    config = configparser.ConfigParser()
    if os.path.exists(_CONFIG_FILE_PATH):
        config.read(_CONFIG_FILE_PATH)
    else:
        print("Config.ini is missing")

    return config[namespace]


def sf_execute(query):
    sf_config = load_config('snowflake')
    conn = snowflake.connector.connect(
        user=sf_config['user'],
        password=sf_config['password'],
        account=sf_config['account'],
        warehouse='compute_wh',
        database=sf_config['database'],
        schema='public',
        role=sf_config['role']
    )
    result = []
    with conn.cursor(cursor_class=snowflake.connector.DictCursor) as cur:
        result = cur.execute(query).fetchall()

    conn.close()

    return result
