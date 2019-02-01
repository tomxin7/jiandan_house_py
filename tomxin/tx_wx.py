import tomxin.tx_request
import uuid
import tomxin.tx_time
import tomxin.tx_mysql
import json
import tomxin.tx_config

def send_wx(msgTo, subject, task, content, open_id, user_name):
    url = "http://wxmsg.dingliqc.com/send"
    model = '''
            {
        "userIds": ["{user_id}"],
        "template_id": "4YscLc2uaCnsdrEdUJ9HGAGAkdBcEQM9bUBy0gs69Hw",
        "url": "{url}",
        "data": {
            "first": {
                "value": "【{subject}】",
                "color": "#d0021b"
            },
            "keyword1": {
                "value": "{send_time}",
                "color": "#173177"
            },
            "keyword2": {
                "value": "来自：简单找房  house.jiandan.live",
                "color": "#173177"
            },
            "remark": {
                "value": "房源地址：{task}",
                "color": "#173177"
            }
        }
    }
    '''

    send_time = tomxin.tx_time.now_time()
    # 把记录插入数据库
    sql = "INSERT INTO info (id, open_id, user_name, task,  create_time, content) VALUES ('{id}', '{open_id}','{user_name}','{task}','{create_time}', '{content}')"
    info_id = str(uuid.uuid1())
    print(info_id)
    sql = sql.replace("{id}", info_id)
    sql = sql.replace("{open_id}", open_id)
    sql = sql.replace("{create_time}", send_time)
    sql = sql.replace("{user_name}", user_name)
    sql = sql.replace("{task}", task)
    sql = sql.replace("{content}", content)
    tomxin.tx_mysql.operate(sql)

    info_url = tomxin.tx_config.get("wx","host") + info_id
    model = model.replace('{user_id}', msgTo)
    model = model.replace('{url}', info_url)
    model = model.replace('{subject}', subject)
    model = model.replace('{send_time}', send_time)
    model = model.replace('{task}', task)
    values = json.loads(model)
    tomxin.tx_request.post_json(url, values)



# if __name__ == '__main__':
#     msgTo = "orPQ808n2X4vtf-1cIihSnbHqisoITWXlbsk3I"
#     subject = "亲爱的Tomxin7，简单找房为你监控到合适的房源"
#     task = "福建福州"
#     open_id = "哈哈哈哈"
#     user_name = "tomxin7"
#
#     info = {}
#     info_list = []
#     info['title'] = "找房找房"
#     info['url'] = "https://zhidao.baidu.com/question/370352847357221604.html"
#     info_list.append(info)
#     info_list.append(info)
#     content = json.dumps(info_list, ensure_ascii=False)  # 将字典装化为json串
#     send_wx(msgTo, subject, task, content, open_id, user_name)
