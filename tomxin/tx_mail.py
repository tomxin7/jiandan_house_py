import smtplib
import email.mime.multipart
import email.mime.text
import random
import time
import tomxin.tx_request
import tomxin.tx_config
class Mail(object):
    msgFrom = ""
    smtpSever = ""
    smtpPort = ""
    sqm = ""
    def __init__(self, msgFrom, smtpSever, smtpPort, sqm):
        self.msgFrom = msgFrom
        self.smtpSever = smtpSever
        self.smtpPort = smtpPort
        self.sqm = sqm


'''
这里存放多个发件邮箱的账号密码，如果经常修改，可以从数据库读取，我这里变化比较少，就不去数据库io了
这四个值分别为
msgFrom  # 从该邮箱发送
smtpSever  # 163邮箱的smtp Sever地址
smtpPort  # 开放的端口
sqm  # 在登录smtp时需要login中的密码应当使用授权码而非账户密码
'''
mailList = []
mailList.append(Mail('jiandan@tomxin.cn', 'smtp.qq.com', '587', ''))
# mailList.append(Mail('17731964024@163.com', 'smtp.163.com', '25', ''))






'''
随机获取邮箱的配置信息
'''
def get_mail_config():
    #生成一个随机数，随机去调用邮箱
    num = random.randint(0, len(mailList)-1)
    #随机返回一个配置
    return mailList[num]


'''
发送简单的邮件，如果失败，不会重试
msgFrom：发送人
msgTo：接收人
subject：主题
content：内容
'''
def send_simple_mail( msgTo, subject, content, mail=get_mail_config()):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = mail.msgFrom
    msg['to'] = msgTo
    msg['subject'] = subject

    content = content
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)

    smtp = smtplib.SMTP()
    smtp.connect(mail.smtpSever, mail.smtpPort)
    smtp.login(mail.msgFrom, mail.sqm)
    smtp.sendmail(mail.msgFrom, msgTo, str(msg))
    smtp.quit()

#增量写入txt文件
def write_new_txt(path,content):
    with open(path, "a",encoding="utf-8") as f:
        f.write(content+"\n")

'''
发送简单的邮件，如果失败，会重复三次，错误会写到本地文件
msgFrom：发送人
msgTo：接收人
subject：主题
content：内容
'''
def retry_simple_mail(msgTo, subject, content):
    error_num = 0
    while(error_num < 3):
        try:
            # 去读取一个配置文件
            mail = get_mail_config()
            send_simple_mail(msgTo, subject, content,  mail)
            return True
        except Exception as e:
            error_num += 1
            write_new_txt("mail_error.txt", str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) +"  " + mail.msgFrom + " 邮箱异常，错误码：" + str(e))
    return False


'''
调用凯闽邮件发送接口，模板邮件
'''
import requests
def send_template_mail_km(msgTo, templet_code, task, subject, url):
    smtp_id = tomxin.tx_config.get("mail", "smtp_id")
    host_url = tomxin.tx_config.get("mail", "url")
    value = {
            "templet_code": templet_code,
            "receiver": msgTo,
            "mail_subject": subject,
            "templet_data": {
                "task": task,
                "url": url

            },
            "smtp_id": smtp_id
        }


    requests.post(url=host_url, json=value)
    # tomxin.tx_request.post_json(url, value)




