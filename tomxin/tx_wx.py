import tomxin.tx_config
import tomxin.tx_request

'''
发送server酱内容
title 标题
message 内容，支持MarkDown
'''
def send_server_jiang(title, message):
    sckey = tomxin.tx_config.get("wx","server_jiang_sckey")
    url = "https://sc.ftqq.com/" + sckey + ".send"
    values = {
        'text': title,
        'desp': message
    }
    tomxin.tx_request.post_not_header(url, values)

'''
发送开发者服务微信
data里面的值，看需求决定参数
user_id 微信推送id
info_url 点击微信需要跳转的地址
'''
def send_dev_wx(user_id, info_url, subject, send_time, task):
    url = "http://wxmsg.dingliqc.com/send"
    values = {
        "userIds": [user_id],
        "template_id": "4YscLc2uaCnsdrEdUJ9HGAGAkdBcEQM9bUBy0gs69Hw",
        "url": info_url,
        "data": {
            "first": {
                "value": "【"+subject+"】",
                "color": "#d0021b"
            },
            "keyword1": {
                "value": send_time,
                "color": "#173177"
            },
            "keyword2": {
                "value": "来自：简单找房  house.jiandan.live",
                "color": "#173177"
            },
            "remark": {
                "value": "房源地址："+ task,
                "color": "#173177"
            }
        }
    }
    tomxin.tx_request.post_json(url, values)


if __name__ == '__main__':
    sckey = "SCU18208Td2023246e4a27d34f7c3b8af152fc3d25a3474469a641"
    title = "121请求13"
    message = "测试"
    send_server_jiang(sckey, title, message)