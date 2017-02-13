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
import termios
import contextlib

import os


@contextlib.contextmanager
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)


def main():
    print 'exit with ^C or ^D'
    with raw_mode(sys.stdin):
        try:
            while True:
                ch = sys.stdin.read(1)
                if not ch or ch == chr(4):
                    break
                # print '%02x,hi' % ord(ch),

                os.system('clear')

        except (KeyboardInterrupt, EOFError):
            pass


if __name__ == '__main__':
    main()
