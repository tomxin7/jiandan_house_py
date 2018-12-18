import tomxin.tx_mysql
import house_info
import house_record
import user_info
import time
import urllib

def houst_main():
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "开始爬取")
    sql = "select city_name,dou_ban_url from city"
    result = tomxin.tx_mysql.select(sql)
    for row in result:
        city = row[0]
        url_num = row[1]

        # 爬取租房信息
        houstList = house_info.getHouse(url_num)

        # 查询改城市需要判断的用户记录
        recordList = house_record.get_record(city)

        # 对比租房信息和用户设置的key
        user_info.check_info(houstList, recordList)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "爬取成功，休息10分钟")
    #休息30分钟
    time.sleep(30 * 60)

    #晚上10点后不再监控
    if str(time.strftime('%H', time.localtime())) == "22":
        print("晚上10点，程序开始休眠")
        time.sleep(60*60*9)

if __name__ == '__main__':
    print("【简单找房】启动成功")
    while(1):
        try:
            houst_main()
        except Exception as e:
            message = "【严重 简单找房】爬虫已结束运行，错误码为：" + str(e)
            message = urllib.parse.quote(message)
            url = "http://wxmsg.dingliqc.com/send?msg=" + message + "&userIds=orPQ808n2X4vtf-1cIihSnbHqisoITWXlbsk3I"
            tomxin.tx_request.get(url)
            exit("程序已退出，错误码："+ str(e))


