#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2017-02-12 星期日
#
#
# 
# @fileOverview 轻踩油门
#
#
# 

import time
import pigpio

pi = pigpio.pi()
if not pi.connected:
    exit(0)

pi.set_servo_pulsewidth(16, 1100)
pi.stop()
