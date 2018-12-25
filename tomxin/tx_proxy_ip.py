# -*- coding: UTF-8 -*-
from urllib import request
import tomxin.tx_request
import tomxin.tx_re
import socket



def get_proxy_ip():
    targeturl = 'https://www.xicidaili.com/nn/' # 验证ip有效性的指定url
    html = tomxin.tx_request.get(targeturl)
    info = tomxin.tx_re.get_first(html, "ip_list", "</table>")
    ip_list = tomxin.tx_re.get_list(info, "img.+?<td>", "</td>")
    port_list = tomxin.tx_re.get_list(info, "img.+?<td>.+?<td>", "</td>")
    i = 0
    proxy_ip_list = []
    for ip in ip_list:
        proxy_ip_list.append(ip + ':' +  port_list[i])
        i = i + 1
    return proxy_ip_list


def proxy_ip_list(url):
    proxy_ip_list = get_proxy_ip()
    ip_list = []
    for ip in proxy_ip_list[:]:
        try:
            socket.setdefaulttimeout(5)
            proxy = {'https': ip}
            proxy_support = request.ProxyHandler(proxy)
            opener = request.build_opener(proxy_support)
            opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
            request.install_opener(opener)
            response = request.urlopen(url)
            if(response.status == 200):
                ip_list.append(ip)
        except Exception as e:
            pass
    return ip_list
