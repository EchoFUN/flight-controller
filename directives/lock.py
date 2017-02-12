#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2017-02-12 星期日
#
#
# 
# @fileOverview 解锁 APM 飞行控制器
#
#
# 

import time
import pigpio

pi = pigpio.pi()
if not pi.connected:
    print('Error connecting to the PIGPIO deamon.')
    exit(0)

# 偏航调动至最右，油门降低到最低维持两秒，既可解锁APM飞控
pi.set_servo_pulsewidth(12, 1100)
pi.set_servo_pulsewidth(16, 1000)

time.sleep(2)
pi.set_servo_pulsewidth(12, 1100)
time.sleep(2)

pi.stop()
