# -*- coding: utf-8 -*-
# @Author : Joy

import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Common import Consts
from Common import Log
from Config import Config


class SendMail:

    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()

    def sendmail(self):
        global smtp
        msg = MIMEMultipart()
        stress_body = Consts.STRESS_LIST
        result_body = Consts.STRESS_LIST
        body = 'Hello, all\n本次运营中心接口自动化测试报告如下：\n   接口相应时间集：%s\n   接口运行结果集： %s\n' \
               % (stress_body, result_body)
        mail_body = MIMEText(body, _subtype='plain', _charset='utf-8')
        tm = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        msg['Subject'] = Header('接口自动化测试报告' + '+' + tm, 'utf-8')
        msg['from'] = self.config.sender
        receivers = self.config.receiver
        # 将收件人分割存list
        toclaue = receivers.split(',')
        msg['To'] = ','.join(toclaue)

        msg.attach(mail_body)

        # noinspection PyBroadException
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.config.smtpserver)
            smtp.login(self.config.username, self.config.password)
            smtp.sendmail(self.config.sender, toclaue, msg.as_string())
        except Exception as e:
            print(e)
            print('发送失败！')
        else:
            print('发送成功！')
            self.log.info('邮件发送成功')
        finally:
            smtp.quit()
