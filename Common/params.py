# -*- coding: utf-8 -*-
# @Author : Joy
# @Explain: 定义测试数据

import os
from Common import commlib
from Common import Log
from Common import Token

log = Log.MyLog()
path_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
print(path_dir)


def get_parameter(name):
    data = commlib.GetPages().get_page_list()
    param = data[name]
    return param


class Login:
    log.info('解析yaml， Path:' + path_dir + '/data/login01.yaml')
    params = get_parameter('Login')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


class GetUserResource:
    log.info('解析yaml，path:' + path_dir + '/data/GetUserResource01.yaml')
    params = get_parameter('GetUserResource')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])


if __name__ == '__main__':
    a = Login
    print(a.url[0])
