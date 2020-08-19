# -*- coding: utf-8 -*-
# @Author : Joy

import requests
from Common import Log
from Config import Config


class Token:
    def __init__(self):
        self.log = Log.MyLog()
        self.config = Config.Config()

    def get_token(self, env):
        """
        获取token
        :param env: 环境变量
        :return:
        """
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }

        if env == 'test':
            login_url = 'http://' + self.config.host_test + self.config.loginHost_test
            parm = self.config.loginInfo_pre
            print(login_url)
            print(parm)

            response = requests.post(login_url, parm, headers=headers)
            result = response.json()
            token_test = result["body"]["info"]["token"]
            self.log.debug('token: %s' % token_test)
            print(result)
            # print(token_test)
            return token_test

        elif env == 'pre':
            login_url = 'http://' + self.config.host_pre + self.config.loginHost_pre
            parm = self.config.loginInfo_pre
            print(login_url)

            response = requests.post(login_url, parm, headers=headers)
            result = response.json()
            token_pre = result["body"]["info"]["token"]
            self.log.debug('token: %s' % token_pre)
            print(result)
            print(token_pre)
            return token_pre

        elif env == 'pro':
            login_url = 'http://' + self.config.host_pro + self.config.loginHost_pro
            parm = self.config.loginInfo_pro
            print(login_url)

            response = requests.post(login_url, parm, headers=headers)
            result = response.json()
            token_pro = result["body"]["info"]["token"]
            self.log.debug('token: %s' % token_pro)
            print(result)
            return token_pro


if __name__ == '__main__':
    to = Token()
    to.get_token('test')