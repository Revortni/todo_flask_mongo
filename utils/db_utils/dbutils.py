import snowflake.connector
from utils.db_utils.snowflake_db import SnowflakeConnector
from utils.db_utils.config_utils import load_config


def sf_execute_v2(query):
    result = []

    print("Creating snowflake connection...")
    connector = SnowflakeConnector()
    with connector.get_connection() as conn:
        with conn.cursor() as cur:
            print("Executing query...")
            result = cur.execute(query).fetchall()

    return result


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
