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

conf.read('apm.conf')


def unlock(ori):
    global pi
    pi = ori

    pi.set_servo_pulsewidth(int(conf.get('Y', 'pin')), 1900)
    pi.set_servo_pulsewidth(int(conf.get('T', 'pin')), 1000)

    time.sleep(3)
    pi.set_servo_pulsewidth(int(conf.get('Y', 'pin')), 1500)


def lock(ori):
    pass


def throttle(value):
    global pi
    pi.set_servo_pulsewidth(int(conf.get('T', 'pin')), value)


def yaw(value):
    global pi
    pi.set_servo_pulsewidth(int(conf.get('Y', 'pin')), value)


def pitch(value):
    global pi
    pi.set_servo_pulsewidth(int(conf.get('P', 'pin')), value)


def modes(value):
    global pi
    pi.set_servo_pulsewidth(int(conf.get('Y', 'pin')), value)


def roll(value):
    global pi
    pi.set_servo_pulsewidth(int(conf.get('R', 'pin')), value)


def hardreset():
    global pi

    sections = conf.sections()
    for i in range(len(sections)):

        sec = sections[i]
        if sec in ['SYS']:
            continue

        pin = int(conf.get(sec, 'pin'))
        ini = int(conf.get(sec, 'ini'))
        pi.set_servo_pulsewidth(pin, ini)