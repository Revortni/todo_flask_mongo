import snowflake.connector

from db.snowflake_db import SnowflakeConnectorV2, SnowflakeConnector
from utils.db_utils.config_utils import load_config, b64_decode

"""
Execute the given query on Snowflake using a SnowflakeConnector object.
"""


def sf_execute_v3(query):
    result = []

    print("Creating snowflake connection...")
    connector = SnowflakeConnector()
    connector.connect()
    result = connector.execute_query(query)

    return result


"""
Execute the given query on Snowflake using a SnowflakeConnector object.
"""


def sf_execute_v2(query):
    result = []

    print("Creating snowflake connection...")
    connector = SnowflakeConnectorV2()
    with connector.connect() as conn:
        with conn.cursor() as cur:
            print("Executing query...")
            result = cur.execute(query).fetchall()

    return result


"""
Execute a SQL query on Snowflake using the provided query string in a single function.
"""


def sf_execute_v1(query):
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
    result = []
    with conn.cursor(cursor_class=snowflake.connector.DictCursor) as cur:
        result = cur.execute(query).fetchall()

    conn.close()

    return result
