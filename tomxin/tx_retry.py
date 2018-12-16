import time

'''
异常处理模块，会重复三次，并记录下错误
调用方式：error_function(e,function_name)
参数
    function：需要被执行的方法
    retry_num：重试次数，默认3次
    sleep_time：休息时间，默认1s
返回值
    True：三次前
    False：三次后
'''

def retry_function(function, retry_num = 3, sleep_time = 1):
    error_num = 0
    while(error_num < retry_num):
        try:
            function
            return True
        except Exception as e:
            error_num += 1
            time.sleep(sleep_time)
    return False


def retry(function):
    function()