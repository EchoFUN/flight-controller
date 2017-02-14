#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2017-02-12 星期日
#
#
# 通过电脑端（发射信号）遥控四轴飞行器飞行；
# 模拟了普通手柄的俯仰、偏航、翻滚、油门，以及切换飞行的模式等等行为，以及智能控制；
#
#
# 

import sys
import time
import pigpio
import readchar
import directives

from excepts import *

from ConfigParser import ConfigParser
conf = ConfigParser()

conf.read('apm.conf')

# 分别为偏航、油门、俯仰、翻滚四个通道
channels = {'YAW': 0, 'THROTTLE': 0, 'PITCH': 0, 'ROLL': 0}
for i in channels.keys():
    channels[i] = conf.get(i, 'pin')


def safelyLand():

    pass


def readerEvent():

    while True:
        key_code = repr(readchar.readkey())
        
        if len(key_code) == 3:
            pass
        elif len(key_code) == 8:

            if key_code[-2] == 'A':    # 上
                channels['THROTTLE'] += 1
                directives.throttle(channels['THROTTLE'])
            elif key_code[-2] == 'B':  # 下
                pass
            elif key_code[-2] == 'C':  # 右
                pass
            elif key_code[-2] == 'D':  # 左
                pass

        # Exit when we  needed. But,  Make the quad landing safely before. 
        if key_code == "'\\x7f'":

            sys.exit('Exit the controller.')
        print(key_code)


def connectPi(url):
    pi = pigpio.pi(url)
    if not pi.connected:
        raise PiConnectError

    return pi


def unlockQuad(pi):
    directives.unlock(pi)


if __name__ == '__main__':

    try:

        # Init the connection to the pigpio GPIO lib.
        # pi = connectPi('192.168.0.1:8080')

        # Unlock the quad first.
        # unlockQuad(pi)

        # Enter the event loop, listening to the key evets.
        readerEvent()

    except EOFError:

        pass
    except PiConnectError:

        # TODO Erorr handling here.
        pass