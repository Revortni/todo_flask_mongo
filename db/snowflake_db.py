from contextlib import contextmanager
import snowflake.connector

from utils.db_utils.config_utils import load_config, b64_decode
from db.interface import DatabaseInterface


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


class SnowflakeConnectorV2():
    @contextmanager
    def connect(self, config=None):
        try:
            print("SnowflakeConnector: Creating connection")
            conn = get_connection(config)
            yield conn
        finally:
            print("SnowflakeConnector: Closing connection")
            conn.close()


class SnowflakeConnector(DatabaseInterface):
    def connect(self, config=None):
        try:
            print("SnowflakeConnector: Creating connection")
            self.conn = get_connection(config)
        except snowflake.connector.Error as e:
            print(f"Unable to connect to database: {str(e)}")

    def close(self):
        print("SnowflakeConnector: Closing connection")
        try:
            self.conn.close()
        except Exception as e:
            print(f"Error occurred while closing connection: {str(e)}")

    def execute_query(self, query, params=None):
        try:
            with self.conn.cursor() as cur:
                print("Executing query...")
                result = cur.execute(query, params).fetchall()
        except Exception as e:
            print(f"Error executing query: {e}")
            result = None
        return result
