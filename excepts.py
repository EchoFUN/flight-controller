#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2017-02-12 星期日
#
#
# 
# 异常指令的封装，这里包含了树莓派的链接异常
#
#
# 

class PiConnectError(Exception):

    def __init__(self):
        self.value = 'Error connecting to the PIGPIO deamon .'


class ExitError(Exception):

    def __init__(self):
        self.value = 'Exit .'
