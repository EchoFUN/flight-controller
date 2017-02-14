#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2017-02-12 星期日
#
#
# 
# @fileOverview APM 飞控中操作指令的封装；包含了飞控的校准，飞行姿态的调整等等命令；
#
#
# 

import time

from ConfigParser import ConfigParser
conf = ConfigParser()


def unlock(pi):

    ch_yaw, ch_throttle = conf.sections('YAW'), conf.sections('THROTTLE')

    pi.set_servo_pulsewidth(ch_yaw.get('pin'), 1900)
    pi.set_servo_pulsewidth(ch_throttle.get('pin'), 1000)

    time.sleep(3)
    pi.set_servo_pulsewidth(ch_yaw.get('pin'), 1500)

    pi.stop()


def unlock():
    pass



def throttle(value):
    pass