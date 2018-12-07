import tomxin.tx_mysql


if __name__ == '__main__':
    sql = "select * from city"
    result = tomxin.tx_mysql.select(sql)
    print(result)