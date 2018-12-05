import tomxin.tx_re
import tomxin.tx_request


if __name__ == '__main__':
    url = "https://www.douban.com/group/255608/"
    html = tomxin.tx_request.get(url)
    info = tomxin.tx_re.get_first(html, '<table class="olt">', '</table>')
    print(info)#去掉头尾，只要列表内容
    title = tomxin.tx_re.get_list(info,'title.+?','end')
    # url = tomxin.tx_re.get_list(info,'start','end')
    # i=0
    # for u in url:
    #     print(u)
    #     print(title[i])
    #     i += 1