from utils.db_utils.sf_dbutils import sf_execute_v1, sf_execute_v2, sf_execute_v3

if __name__ == '__main__':
    print(sf_execute_v1('select * from product_analysis_mv limit 10;'))
    print(sf_execute_v2('select * from product_analysis_mv limit 10;'))
    print(sf_execute_v3('select * from product_analysis_mv limit 10;'))
