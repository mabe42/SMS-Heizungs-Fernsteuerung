#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from time import sleep

timeformat = "%y-%m-%d %H:%M  "
DayL = ['mon','tue','wed','thu','fri','sat','sun']
date = DayL[datetime.datetime.today().weekday()] 
now = datetime.datetime.now()
timenow = now.strftime(timeformat)
#print (timenow)
logname = "".join([date, ".log"])
datafile = open(logname, "a")
temperaturfile = open("/home/mabe42/temperatur.log", "a")
# the sensor id needs to be adapted to that of the sensor present
tfile = open("/sys/bus/w1/devices/10-000802e75cf1/w1_slave")
temperature = 85.0
while temperature == 85.0:
  text = tfile.read()
  temperature_data = text.split()[-1]
  temperature = float(temperature_data[2:])
  temperature = temperature / 1000
#  print (temperature)
  sleep(10)
tfile.close()
datafile.write(str(temperature) + "\n")
temperaturfile.write("20" + timenow + str(temperature) + "\n")
datafile.close()
temperaturfile.close()

