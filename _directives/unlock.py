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

def run():
    # 偏航调动至最右，油门降低到最低维持两秒以上，既可解锁APM飞控；解锁完成后回拨偏航摇杆；
    pi.set_servo_pulsewidth(12, 1900)
    pi.set_servo_pulsewidth(16, 1000)

    time.sleep(3)
    pi.set_servo_pulsewidth(12, 1500)

    pi.stop()
