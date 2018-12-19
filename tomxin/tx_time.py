import time

def now_time():
    return str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))