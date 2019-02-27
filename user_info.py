import tomxin.tx_mail
import tomxin.tx_mysql
import tomxin.tx_time
import tomxin.tx_wx
import uuid
import json

def check_info(houstList, recordList):
    for record in recordList:
        key_word = str(record.key_word)
        key_list = key_word.split(",")
        msgTo = record.remind
        flag = ""
        info_list = []
        selectSql = "select id from remind where user_id = '{user_id}' and record_id = '{record_id}'"
        insertSql = "INSERT INTO remind (user_id, city, record_id,add_time) VALUES ('{user_id}', '{city}', '{record_id}','{add_time}') "
        for key in key_list:
            for houst in houstList:
                if key in houst.title or key in houst.content:
                    s_sql = selectSql.replace("{user_id}", record.open_id)
                    s_sql = s_sql.replace("{record_id}", houst.url[-10:-1])
                    #查询数据库中，这条记录是否已经发送过了
                    s_row = tomxin.tx_mysql.select(s_sql)
                    if len(s_row) == 0:
                        flag = 1
                        info = {}
                        info['title'] = houst.title.replace("\\","")
                        info['url'] = houst.url
                        info_list.append(info)
                        #插入已发送标识
                        i_sql = insertSql.replace("{user_id}", record.open_id)
                        i_sql = i_sql.replace("{city}", record.city_name)
                        i_sql = i_sql.replace("{add_time}", tomxin.tx_time.now_time())
                        i_sql = i_sql.replace("{record_id}", houst.url[-10:-1])
                        tomxin.tx_mysql.operate(i_sql)

        if flag != "":
            send_time = tomxin.tx_time.now_time()
            info_id = str(uuid.uuid1())
            open_id = record.open_id
            user_name = "用户"
            task = record.city_name + "-" + record.key_word
            content = json.dumps(info_list, ensure_ascii=False)  # 将字典装化为json串
            info_url = tomxin.tx_config.get("wx", "host") + info_id
            subject = "简单找房为你监控到合适的房源，请及时查看"

            # 把记录插入数据库
            sql = "INSERT INTO info (id, open_id, user_name, task,  create_time, content) VALUES ('{id}', '{open_id}','{user_name}','{task}','{create_time}', '{content}')"
            sql = sql.replace("{id}", info_id)
            sql = sql.replace("{open_id}", open_id)
            sql = sql.replace("{create_time}", send_time)
            sql = sql.replace("{user_name}", user_name)
            sql = sql.replace("{task}", task)
            sql = sql.replace("{content}", content)
            tomxin.tx_mysql.operate(sql)

            # 发送消息
            if record.remind_type == "邮箱":
                templet_code = "house"
                tomxin.tx_mail.send_template_mail_km(msgTo, templet_code, task, subject, info_url)

            if record.remind_type == "微信":
                tomxin.tx_wx.send_dev_wx(msgTo, info_url, subject, send_time, task)

            print(msgTo + "发送成功")