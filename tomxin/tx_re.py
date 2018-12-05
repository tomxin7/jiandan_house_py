import re

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