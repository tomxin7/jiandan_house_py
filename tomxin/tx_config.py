import configparser

import os

#获取当前项目根目录
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

config = configparser.ConfigParser()
config.read(root_path + "/tomxin/base.cfg")

'''
获取配置
'''
def get(section, name):
    return config.get(section, name)

