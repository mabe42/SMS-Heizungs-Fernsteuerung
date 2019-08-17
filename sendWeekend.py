#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os

DayL = ['fri','sat','sun']
# the sensor id needs to be adapted to that of the sensor present
tfile = open("/sys/bus/w1/devices/10-000802e75cf1/w1_slave")
text = tfile.read()
tfile.close()

temperature_data = text.split()[-1]
temperature = float(temperature_data[2:])
temperature = temperature / 1000
#print(temperature)

output = ""
for day in DayL:
  avgname = day+".avg"
  avgfile = open(avgname, "r")
  dayavg = avgfile.read()
#  print(dayavg)
  avgfile.close()
  output += dayavg

output = output + "now " + '{:03.1f}'.format(temperature) 
cfile = open("/home/mabe42/content", "w")
cfile.write(output)
cfile.close()

lfile = open("/home/mabe42/smslogfile.log", "a")
lfile.write("sendWeekend.py wrote content\n")
lfile.close
