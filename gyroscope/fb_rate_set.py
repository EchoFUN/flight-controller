#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2017-01-21 星期日
#
#
# #fileOverview 陀螺仪回传速率设置，默认情况下是 10hz，一秒钟回传十个数据包
#
#
#

import serial

sensor = serial.Serial(port='/dev/ttyAMA0', baudrate='9600', timeout=1)

sensor.write('\xff')