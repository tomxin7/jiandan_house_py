import tomxin.tx_mysql
import main.house_info

title = ""
url = ""
content = ""


if __name__ == '__main__':
    sql = "select * from city"
    result = tomxin.tx_mysql.select(sql)
    for row in result:
        city = row[1]
        url_num = row[2]
        main.house_info.getUserHouse(city, url_num)
