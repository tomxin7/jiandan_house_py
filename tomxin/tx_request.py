from urllib import parse,request
import urllib
import socket
import ssl
import json
ssl._create_default_https_context = ssl._create_unverified_context

'''
普通的get请求
'''
def get(url):
    timeout = 10  # 这里是设置超时时间
    socket.setdefaulttimeout(timeout)
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"})
    oper = urllib.request.urlopen(req)
    return oper.read().decode("utf-8")

'''
自定义编码格式的请求
'''
def get_encoding(url, encoding):
    timeout = 10  # 这里是设置超时时间
    socket.setdefaulttimeout(timeout)
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"})
    oper = urllib.request.urlopen(req)
    return oper.read().decode(encoding)

'''
post请求
'''
import urllib.request
'''
url = 'http://jobsky.csu.edu.cn/Home/PartialArticleList'
values = {
    'pageindex': '1',
    'pagesize': '15',
    'typeid':'4',
    'followingdates':'-1'
}
'''
def post(url,values):
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
    data = urllib.parse.urlencode(values)
    # that params output from urlencode is encoded to bytes before it is sent to urlopen as data
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data, headers=header_dict)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html.decode('utf-8')

'''
指定编码格式的post请求
'''
def post_encoding(url, values, encoding):
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
    data = urllib.parse.urlencode(values)
    # that params output from urlencode is encoded to bytes before it is sent to urlopen as data
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data, headers=header_dict)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html.decode(encoding)


'''
当需要传输的数据是json格式的时候使用
'''
def post_json(url, value):
    value = json.dumps(value).encode(encoding='utf-8')
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
    req = request.Request(url=url,data=value,headers=headers)
    res = request.urlopen(req)
    res = res.read()
    return res.decode(encoding='utf-8')

'''
当需要传输的数据是json格式的时候使用
url = 'http://jobsky.csu.edu.cn/Home/PartialArticleList'
values = {
    'pageindex': '1',
    'pagesize': '15',
    'typeid':'4',
    'followingdates':'-1'
}
'''
def post_json_headers(url, value, headers):
    value = json.dumps(value).encode(encoding='utf-8')
    #普通数据使用
    req = request.Request(url=url,data=value,headers=headers)
    res = request.urlopen(req)
    res = res.read()
    return res.decode(encoding='utf-8')

'''
当需要传输的数据是json格式的时候使用
url = 'http://jobsky.csu.edu.cn/Home/PartialArticleList'
values = {
    'pageindex': '1',
    'pagesize': '15',
    'typeid':'4',
    'followingdates':'-1'
}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
'''
def post_headers(url, value, headers):
    value = parse.urlencode(value).encode(encoding='utf-8')
    req = request.Request(url=url,data=value,headers=headers)
    res = request.urlopen(req)
    res = res.read()
    return res.decode(encoding='utf-8')