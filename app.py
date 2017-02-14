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

import os
import time
import pigpio
import readchar
import director

from excepts import *

from ConfigParser import ConfigParser
conf = ConfigParser()

conf.read('apm.conf')
STEP = int(conf.get('SYS', 'step'))

# 分别为偏航、油门、俯仰、翻滚四个通道
channels = {'Y': 0, 'T': 0, 'P': 0, 'R': 0}
for i in channels.keys():
    channels[i] = int(conf.get(i, 'ini'))


def safelyLand():

    pass


def channelPrinter():
    os.system('clear')
    for i in channels.keys():
        print(i + ': ' + str(channels[i]))


def readerEvent():

    while True:
        code = repr(readchar.readkey())
        token = code[-2]

        if len(code) == 3:

            # 模式
            if token in ['1', '2', '3', '4']:
                director.modes(token)
            # 仰
            elif token == 'w':
                channels['P'] += STEP
                director.pitch(channels['R'])
            # 俯
            elif token == 's':
                channels['P'] -= STEP
                director.pitch(channels['R'])
            # 左翻转
            elif token == 'a':
                channels['R'] += STEP
                director.throttle(channels['R'])
            # 右翻转
            elif token == 'd':
                channels['R'] -= STEP
                director.throttle(channels['R'])

        elif len(code) == 8:

            # 加油
            if token == 'A':
                channels['T'] += STEP
                director.throttle(channels['T'])
            # 减油
            elif token == 'B':
                channels['T'] -= STEP
                director.throttle(channels['T'])
            # 右偏航
            elif token == 'C':
                channels['Y'] += STEP
                director.yaw(channels['Y'])
            # 左偏航
            elif token == 'D':
                channels['Y'] -= STEP
                director.yaw(channels['Y'])

        # Exit when we  needed. But,  Make the quad landing safely before. 
        if code == "'\\x7f'":
            raise ExitError

        channelPrinter()


def connectPi(url, port):
    pi = pigpio.pi(url, port)
    if not pi.connected:
        raise PiConnectError

    return pi


def unlockQuad(pi):
    director.unlock(pi)


if __name__ == '__main__':

    try:

        # Init the connection to the pigpio GPIO lib.
        print('connected to the pi ...')
        pi = connectPi(conf.get('SYS', 'url'), '8888')
        print('connected !')

        # Unlock the quad first.
        print('unlock the quad ...')
        unlockQuad(pi)
        print('unlocked !')

        # Enter the event loop, listening to the key evets.
        channelPrinter()
        readerEvent()

    except EOFError:

        pass
    except PiConnectError:

        # TODO Erorr handling here.
        pass

    except ExitError:
        pass