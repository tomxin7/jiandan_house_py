import tomxin.tx_re
import tomxin.tx_request
import time

class House(object):
    title = ""
    url = ""
    content = ""
    def __init__(self, title, url, content):
        self.title = title
        self.url = url
        self.content = content

'''
获取详情
'''
def getDetils(url):
    html = tomxin.tx_request.get(url)
    content = tomxin.tx_re.get_first(html,'Conversation.+?text": "','"name": "')
    return content

'''
获取信息列表
'''
def getHoustList(url):
    html = tomxin.tx_request.get(url)
    info = tomxin.tx_re.get_first(html, '<table class="olt">', '</table>')
    titleList = tomxin.tx_re.get_list(info,'title="','"')
    urlList = tomxin.tx_re.get_list(info,'class="title".+?"','"')
    i=0
    houseList = []
    for url in urlList[:]:
        conten = getDetils(url)
        house = House(title= titleList[i], url= url, content=conten)
        houseList.append(house)
        time.sleep(2)
        i += 1
    return houseList


    # for house in houseList:
    #     if "鼓楼" in house.content or "鼓楼" in house.title:
    #         print(house.title)
    #         print(house.url)
