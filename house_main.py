import tomxin.tx_mysql
import house_info
import house_record
import user_info
import time

if __name__ == '__main__':
    while(1):
        sql = "select city_name,dou_ban_url from city"
        result = tomxin.tx_mysql.select(sql)
        for row in result:
            city = row[0]
            url_num = row[1]

            #爬取租房信息
            houstList = house_info.getHouse(url_num)

            #查询改城市需要判断的用户记录
            recordList = house_record.get_record(city)

            user_info.check_info(houstList, recordList)

        time.sleep(10*60)

