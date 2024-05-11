import snowflake.connector
from contextlib import contextmanager

from utils.config_utils import load_config, b64_decode

# class SnowflakeConnector(object):
#     def __init__(self, config):
#         self.conn = None
#         self.config = config

#     def __enter__(self):
#         print("SnowflakeConnector: Creating connection")
#         self.conn = get_connection(self.config)
#         return self.conn

#     def __exit__(self, *args):
#         print("SnowflakeConnector: Closing connection")
#         self.conn.close()


class SnowflakeConnector(object):
    def __init__(self, config=None):
        self.config = config

    @contextmanager
    def get_connection(self):
        try:
            print("SnowflakeConnector: Creating connection")
            conn = get_connection(self.config)
            yield conn
        finally:
            print("SnowflakeConnector: Closing connection")
            conn.close()


def get_connection(sf_config):
    if not sf_config:
        sf_config = load_config('snowflake')

    conn = snowflake.connector.connect(
        user=sf_config['user'],
        password=b64_decode(sf_config['password']),
        account=sf_config['account'],
        warehouse='compute_wh',
        database=sf_config['database'],
        schema='public',
        role=sf_config['role']
    )

    return conn
