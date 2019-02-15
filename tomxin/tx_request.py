from urllib import parse,request
import urllib
import socket
import ssl
import json
import tomxin.tx_time
ssl._create_default_https_context = ssl._create_unverified_context

'''
普通的get请求
'''
def get(url):
    try:
        timeout = 30  # 这里是设置超时时间
        socket.setdefaulttimeout(timeout)
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"})
        oper = urllib.request.urlopen(req)
        return oper.read().decode("utf-8")
    except Exception as e:
        print(tomxin.tx_time.now_time() + "【普通的get请求异常】get(url) url：" + url)
        raise e#抛出这个异常


'''
有代理ip的get请求
'''
def get_proxy(url,ip):
    try:
        proxy = {'https': ip}
        proxy_support = request.ProxyHandler(proxy)
        opener = request.build_opener(proxy_support)
        opener.addheaders = [('User-Agent',
                              'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
        request.install_opener(opener)
        response = request.urlopen(url)
        return response.read().decode("utf-8")
    except Exception as e:
        print(tomxin.tx_time.now_time() + "【get请求异常】get_proxy(url,ip) url：%s  ip:%s"  %(url, ip))
        raise e#抛出这个异常

'''
自定义编码格式的请求
'''
def get_encoding(url, encoding):
    try:
        timeout = 30  # 这里是设置超时时间
        socket.setdefaulttimeout(timeout)
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"})
        oper = urllib.request.urlopen(req)
        return oper.read().decode(encoding)
    except Exception as e:
        print(tomxin.tx_time.now_time() + "【get请求异常】get_encoding(url, encoding) url：%s  encoding:%s"  %(url, encoding))
        raise e#抛出这个异常

'''
带请求头的get请求
headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"}
'''
def get_headers(url, headers):
    try:
        timeout = 30  # 这里是设置超时时间
        socket.setdefaulttimeout(timeout)
        req = urllib.request.Request(url, headers=headers)
        oper = urllib.request.urlopen(req)
        return oper.read().decode("utf-8")
    except Exception as e:
        print(tomxin.tx_time.now_time() + "【get请求异常】get_headers(url, headers) url：%s  headers:%s"  %(url, headers))
        raise e#抛出这个异常
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
    try:
        header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                       "Content-Type": "application/json"}
        data = urllib.parse.urlencode(values)
        # that params output from urlencode is encoded to bytes before it is sent to urlopen as data
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data, headers=header_dict)
        response = urllib.request.urlopen(req)
        html = response.read()
        return html.decode('utf-8')
    except Exception as e:
        print(tomxin.tx_time.now_time() + "【post请求异常】 post(url,values) url：%s  values:%s"  %(url, values))
        raise e#抛出这个异常
'''
指定编码格式的post请求
'''
def post_encoding(url, values, encoding):
    try:
        header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                       "Content-Type": "application/json"}
        data = urllib.parse.urlencode(values)
        # that params output from urlencode is encoded to bytes before it is sent to urlopen as data
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data, headers=header_dict)
        response = urllib.request.urlopen(req)
        html = response.read()
        return html.decode(encoding)
    except Exception as e:
        print(tomxin.tx_time.now_time() + "【post请求异常】 post_encoding(url, values, encoding) url：%s  values:%s encoding:%s"  %(url, values, encoding))
        raise e#抛出这个异常

'''
当需要传输的数据是json格式的时候使用
'''
def post_json(url, value):
    try:
        value = json.dumps(value).encode(encoding='utf-8')
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json"}
        req = request.Request(url=url, data=value, headers=headers)
        res = request.urlopen(req)
        res = res.read()
        return res.decode(encoding='utf-8')
    except Exception as e:
        print(tomxin.tx_time.now_time() + "【post请求异常】 post_json(url, value) url：%s  values:%s"  %(url, value))
        raise e#抛出这个异常

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
    try:
        value = json.dumps(value).encode(encoding='utf-8')
        # 普通数据使用
        req = request.Request(url=url, data=value, headers=headers)
        res = request.urlopen(req)
        res = res.read()
        return res.decode(encoding='utf-8')
    except Exception as e:
        print(tomxin.tx_time.now_time() + "【post请求异常】 post_json_headers(url, value, headers) url：%s  values:%s  headers:%s"  %(url, value, headers))
        raise e#抛出这个异常
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
    try:
        value = parse.urlencode(value).encode(encoding='utf-8')
        req = request.Request(url=url, data=value, headers=headers)
        res = request.urlopen(req)
        res = res.read()
        return res.decode(encoding='utf-8')
    except Exception as e:
        print(tomxin.tx_time.now_time() + "【post请求异常】 post_headers(url, value, headers) url：%s  values:%s  headers:%s"  %(url, value, headers))
        raise e#抛出这个异常

'''
post请求不带请求头
url = 'http://jobsky.csu.edu.cn/Home/PartialArticleList'
values = {
    'pageindex': '1',
    'pagesize': '15',
    'typeid':'4',
    'followingdates':'-1'
}
'''
def post_not_header(url,values):
    try:
        data = urllib.parse.urlencode(values)
        # that params output from urlencode is encoded to bytes before it is sent to urlopen as data
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)
        response = urllib.request.urlopen(req)
        html = response.read()
        return html.decode('utf-8')
    except Exception as e:
        print(tomxin.tx_time.now_time() + "【post请求异常】 post(url,values) url：%s  values:%s"  %(url, values))
        raise e#抛出这个异常