import tomxin.tx_mysql
import main.house_info

title = ""
url = ""
content = ""


if __name__ == '__main__':
    sql = "select * from city"
    result = tomxin.tx_mysql.select(sql)
    houstList = []
    for row in result:
        city = row[1]
        url_num = row[2]
        # houstList = main.house_info.getHouse(url_num)
        user_sql = "select * from record where city_name = " + "'"+  city +"'"
        user_result = tomxin.tx_mysql.select(user_sql)
        print(1)
