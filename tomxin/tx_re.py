import re
import pymysql

'''
正则表达式返回整个匹配的列表
'''
def get_list(info, reStart, reEnd):
    regex = r'' + reStart + '(.*?)' + reEnd
    pat=re.compile(regex,re.S)
    content = re.findall(pat,info)
    return content


'''
正则表达式只返回第一个匹配的
'''
def get_first(info, reStart, reEnd):
    regex = r''+reStart+'(.*?)'+reEnd
    pat=re.compile(regex,re.S)
    content = re.findall(pat,info)
    return content[0]

'''
过滤emoji表情
'''
def filter_emoji(desstr, restr=''):
    try:
        co = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        co = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return co.sub(restr, desstr)

'''
正则表达式只返回第一个匹配的，但是HTML经过了处理
'''
def get_first_html_foram(info, reStart, reEnd):
    regex = r''+reStart+'(.*?)'+reEnd
    pat=re.compile(regex,re.S)
    content = re.findall(pat,info)
    content = pymysql.escape_string(str(content[0]))
    content = filter_emoji(content)
    return content


