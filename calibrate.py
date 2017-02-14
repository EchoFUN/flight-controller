#!/usr/bin/env python
# -*- coding: utf-8 -*

#
# @author XU Kai(xukai.ken@gmail.com)
# @date 2017-02-12 星期日
#
#
# 
# @fileOverview 校准 APM 飞控，调高和调低六个通道的边界值；遥控器校准；
#
#
# 

import time
import sys
import pigpio

from ConfigParser import ConfigParser
conf = ConfigParser()

conf.read('apm.conf')

pi = pigpio.pi(conf.get('SYS', 'url'), '8888')
if not pi.connected:
    sys.exit('Error !')

sections = conf.sections()


try:
    for i in range(len(sections)):

        sec = sections[i]
        if sec in ['SYS']:
            continue

        pin = int(conf.get(sec, 'pin'))
        print('Pwm on pin ' + str(pin))
        pi.set_servo_pulsewidth(pin, int(conf.get(sec, 'min')))
        time.sleep(0.5)
        pi.set_servo_pulsewidth(pin, int(conf.get(sec, 'max')))
        time.sleep(0.5)
        pi.set_servo_pulsewidth(pin, int(conf.get(sec, 'ini')))
        time.sleep(0.5)

    pi.stop()
    sys.exit('Done !')

except ValueError:
    sys.exit('config file error !')
    pi.stop()