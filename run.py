# -*- coding: utf-8 -*-
# @Author : Joy

import sys
import pytest

from Common import Log
from Common import Shell
from Config import Config

if __name__ == '__main__':
    conf = Config.Config()
    log = Log.MyLog()
    log.info('初始化配置文件，path=' + conf.conf_path + '\n')

    shell = Shell.Shell()
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    # 定义测试集
    # allure_list = '--allure_features=Home,Personal'

    # allure报告清空上一次运行的记录
    args = ['-s', '-q', '--alluredir', xml_report_path, conf.xml_report_path]

    # log.info('执行用例集：%s' % allure_list)
    # self_args = sys.argv[1:]
    # sys.argv 是命令行参数列表  args: 要解析的命令行参数列表
    pytest.main(args)
    cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path + '--clean')

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise
