import tomxin.tx_re
import tomxin.tx_request


if __name__ == '__main__':
    url = ""
    html = tomxin.tx_request.get(url)
    print(html)#获取网页源码，如果报错，可能是上面编码的问题
    # info = tomxin.tx_re.get_first(html, 'start', 'end')
    # print(info)#去掉头尾，只要列表内容
    # title = tomxin.tx_re.get_list(info,'start','end')
    # url = tomxin.tx_re.get_list(info,'start','end')
    # i=0
    # for u in url:
    #     print(u)
    #     print(title[i])
    #     i += 1