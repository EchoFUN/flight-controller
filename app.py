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

import ConfigParser


def safelyLand():

    pass

def readerEvent():

    while True:
        key_code = repr(readchar.readkey())
        print(key_code)

        # Exit when we  needed. But,  Make the quad landing safely before. 
        if key_code == "'\\x7f'":

            sys.exit('Exit the controller.')


def connectPi():
    pi = pigpio.pi()
    if not pi.connected:
        print('Error connecting to the PIGPIO deamon.')
        sys.exit()

    return pi


import unlock from directives
def unlockQuad():

    pass


if __name__ == '__main__':

    try:

        # Init the connection to the pigpio GPIO lib.
        pi = connectPi()

        # Unlock the quad first.
        unlockQuad(pi)

        # Enter the event loop, listening to the key evets.
        readerEvent()

    except EOFError:

        # TODO Erorr handling here.
        pass