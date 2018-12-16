import tomxin.tx_mail
import time

content_tail = "\n\n------------------------------------------------------------\n\n\n网上信息存在不确定性，请您务必核实信息真实性\n\n如需要取消提醒，请登录网站：\nhttp://house.jiandan.live\n进入个人中心，终止监控任务\n\n如果您受到骚扰，或者是系统问题\n请直接联系QQ：1341749898"
def check_info(houstList, recordList):
    for record in recordList:
        key_word = str(record.key_word)
        key_list = key_word.split(",")
        msgTo = record.remind
        content = ""
        for key in key_list:
            for houst in houstList:
                if key in houst.title or key in houst.content:
                    content = content + "\n" +  houst.title + houst.url +"\n\n"
        if content != "":
            if record.remind_type == "邮箱":
                content_head = "您的任务【city_remind】\n监控到以下房源，请复制网址到浏览器打开：\n\n------------------------------------------------------------\n\n"
                now_date = time.strftime("%m-%d %H:%M", time.localtime())
                subject = "【简单找房】" + now_date + "最新房源提醒"
                content_head = content_head.replace("city_remind", record.city_name + "-" + record.key_word)
                content = content_head + content + content_tail
                tomxin.tx_mail.retry_simple_mail(msgTo, subject, content)

#
# if __name__ == '__main__':
#     msgTo = "865498311@qq.com"
#     now_date = time.strftime("%m-%d %H:%M", time.localtime())
#     subject = "【简单找房】" + now_date + "最新房源提醒"
#     content_head = "您的任务【city_remind】\n监控到以下房源，请复制网址到浏览器打开：\n\n------------------------------------------------------------\n\n"
#     content = "龙华民治 1980次卧 高档小区 房东直租\nhttps://www.douban.com/group/topic/129424016/\n\n龙华民治 1980次卧 高档小区 房东直租\nhttps://www.douban.com/group/topic/129424016/"
#     content_tail = "\n\n------------------------------------------------------------\n\n\n网上信息存在不确定性，请您务必核实信息真实性\n\n如需要取消提醒，请登录网站：\nhttp://house.jiandan.live\n进入个人中心，终止监控任务\n\n如果您受到骚扰，或者是系统问题\n请直接联系QQ：1341749898"
#     content = content_head + content + content_tail
#     tomxin.tx_mail.retry_simple_mail(msgTo, subject, content)