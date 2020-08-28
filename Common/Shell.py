# -*- coding: utf-8 -*-
# @Author : Joy

import subprocess
# subprocess 模块允许我们启动一个新进程，并连接到它们的输入/输出/错误管道，从而获取返回值。


class Shell:
    @staticmethod
    def invoke(cmd):
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o
# stdin、stdout 和 stderr：子进程的标准输入、输出和错误。
# subprocess.PIPE 表示为子进程创建新的管道