from utils.db_utils.dbutils import sf_execute, sf_execute_v2


def get_top_items_sold():
    query = '''select * from PRODUCT_ANALYSIS_MV order by items_sold desc limit 1;'''
    result = sf_execute_v2(query)

    print(result)


get_top_items_sold()
