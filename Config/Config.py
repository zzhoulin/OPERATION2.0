# -*- coding: utf-8 -*-
# @Author : Joy


from configparser import ConfigParser
from Common import Log
import os


class Config:
    # 定义title
    TITLE_TEST = 'private_test'
    TITLE_PRE = 'private_pre'
    TITLE_PRO = 'private_pro'
    TITLE_EMAIL = 'mail'

    # value [test/pre/pro]
    VALUE_TESTER = 'tester'
    VALUE_ENVIRONMENT = 'environment'
    VALUE_VERSION = 'version'
    VALUE_HOST = 'host'
    VALUE_LOGINHOST = 'loginhost'
    VALUE_LOGININFO = 'logininfo'

    # mail
    VALUE_SMTPSERVER = 'smtpserver'
    VALUE_SENDER = 'sender'
    VALUE_RECEIVER = 'receiver'
    VALUE_USERNAME = 'username'
    VALUE_PASSWORD = 'password'

    # 获取项目path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = Log.MyLog()
        # ini配置文件路径
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir + "/Report/xml"
        self.html_report_path = Config.path_dir + "/Report/html"

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        # 读取配置文件
        self.config.read(self.conf_path, encoding='utf-8')

        # TEST 测试环境
        self.tester_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_TESTER)
        self.environment_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_ENVIRONMENT)
        self.version_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_VERSION)
        self.host_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_HOST)
        self.loginHost_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_LOGINHOST)
        self.loginInfo_test = self.get_conf(Config.TITLE_TEST, Config.VALUE_LOGININFO)

        # PRE 预发环境
        self.tester_pre = self.get_conf(Config.TITLE_PRE, Config.VALUE_TESTER)
        self.environment_pre = self.get_conf(Config.TITLE_PRE, Config.VALUE_ENVIRONMENT)
        self.version_pre = self.get_conf(Config.TITLE_PRE, Config.VALUE_VERSION)
        self.host_pre = self.get_conf(Config.TITLE_PRE, Config.VALUE_HOST)
        self.loginHost_pre = self.get_conf(Config.TITLE_PRE, Config.VALUE_LOGINHOST)
        self.loginInfo_pre = self.get_conf(Config.TITLE_PRE, Config.VALUE_LOGININFO)

        # PRO 生产环境
        self.tester_pro = self.get_conf(Config.TITLE_PRO, Config.VALUE_TESTER)
        self.environment_pro = self.get_conf(Config.TITLE_PRO, Config.VALUE_ENVIRONMENT)
        self.version_pro = self.get_conf(Config.TITLE_PRO, Config.VALUE_VERSION)
        self.host_pro = self.get_conf(Config.TITLE_PRO, Config.VALUE_HOST)
        self.loginHost_pro = self.get_conf(Config.TITLE_PRO, Config.VALUE_LOGINHOST)
        self.loginInfo_pro = self.get_conf(Config.TITLE_PRO, Config.VALUE_LOGININFO)

        # email
        self.smtpserver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SMTPSERVER)
        self.sender = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SENDER)
        self.receiver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_RECEIVER)
        self.username = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_USERNAME)
        self.password = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_PASSWORD)

    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)


if __name__ == "__main__":
    con = Config()
    print(con)
