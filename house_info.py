import tomxin.tx_re
import tomxin.tx_request
import time
import tomxin.tx_mysql
import tomxin.tx_time
import tomxin.tx_proxy_ip


class House(object):
    title = ""
    url = ""
    content = ""

    def __init__(self, title, url, content):
        self.title = title
        self.url = url
        self.content = content


#2、按行读取并存为list
def open_txt_list(path):
    file_object = open(path,"r", encoding='utf-8')
    txt_list=[]
    try:
        for line in file_object:
            txt_list.append(str(line).replace("\n",""))
    finally:
        file_object.close()
    return txt_list


'''
获取详情
'''
def getDetils(url):
    while(1):
        try:
            ip_list = open_txt_list("ip.txt")
            ip = ip_list[0]
            html = tomxin.tx_request.get_proxy(url, ip)
            content = tomxin.tx_re.get_first_html_foram(html, 'Conversation.+?text": "', '"name": "')
            break
        except Exception as e:
            print("抓取信息详情发生异常，准备切换ip")
            tomxin.tx_proxy_ip.judge_proxy_ip(url)
    return content


'''
获取信息列表
'''


def getHoustList(url):
    while(1):
        try:
            ip_list = open_txt_list("ip.txt")
            ip = ip_list[0]
            html = tomxin.tx_request.get_proxy(url, ip)
            info = tomxin.tx_re.get_first(html, '<table class="olt">', '</table>')
            titleList = tomxin.tx_re.get_list(info, 'title="', '"')
            urlList = tomxin.tx_re.get_list(info, 'class="title".+?"', '"')
            break
        except Exception as e:
            print("抓取列表信息发生异常，准备切换ip")
            tomxin.tx_proxy_ip.judge_proxy_ip(url)
    i = 0
    houseList = []
    for url in urlList[:]:
        # 如果是pl，代表是置顶的推广
        if url == "pl":
            i += 1
            continue
        # 先去查询这条数据是不是被爬取过了
        id = url[-10:-1]
        sql = "select content from house where id = '{id}'"
        sql = sql.replace("{id}", id)
        row = tomxin.tx_mysql.select(sql)
        if (len(row) == 0):
            content = getDetils(url)
            sql = "INSERT INTO house (id, title, url, content, add_time) VALUES ('{id}', '{title}','{url}', '{content}', '{add_time}')"
            sql = sql.replace("{id}", id)
            sql = sql.replace("{title}", titleList[i])
            sql = sql.replace("{url}", url)
            sql = sql.replace("{content}", content)
            sql = sql.replace("{add_time}", tomxin.tx_time.now_time())
            try:
                tomxin.tx_mysql.operate(sql)
            except Exception as e:
                print("信息详情插入数据库错误，跳过该条数据")
        else:
            content = row[0]
        house = House(title=titleList[i], url=url, content=content)
        houseList.append(house)
        # 每一次要休息一会
        time.sleep(3)
        i += 1
    return houseList


'''
查询
'''


def getHouse(url_num):
    url_num = url_num.split(",")
    houstList = []
    for url in url_num:
        houstList += getHoustList("https://www.douban.com/group/" + url)
    return houstList
