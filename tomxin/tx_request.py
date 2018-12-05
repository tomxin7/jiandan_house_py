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
    # json串数据使用
    value = json.dumps(value).encode(encoding='utf-8')
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
    req = request.Request(url=url,data=value,headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    return (res.decode('utf-8'))

# def post(url, value, )
# textmod={"jsonrpc": "2.0","method":"user.login","params":{"user":"admin","password":"zabbix"},"auth": None,"id":1}
# #json串数据使用
# textmod = json.dumps(textmod).encode(encoding='utf-8')
# #普通数据使用
# textmod = parse.urlencode(textmod).encode(encoding='utf-8')
# print(textmod)
# #输出内容:b'{"params": {"user": "admin", "password": "zabbix"}, "auth": null, "method": "user.login", "jsonrpc": "2.0", "id": 1}'
# header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
# url='http://192.168.199.10/api_jsonrpc.php'
# req = request.Request(url=url,data=textmod,headers=header_dict)
# res = request.urlopen(req)
# res = res.read()
# print(res)
# #输出内容:b'{"jsonrpc":"2.0","result":"37d991fd583e91a0cfae6142d8d59d7e","id":1}'
# print(res.decode(encoding='utf-8'))
# #输出内容:{"jsonrpc":"2.0","result":"37d991fd583e91a0cfae6142d8d59d7e","id":1}