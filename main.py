from dbutils import sf_execute


def get_top_items():
    query = '''select * from PRODUCT_ANALYSIS_MV order by items_sold desc limit 1;'''
    result = sf_execute(query)

    print(result)
