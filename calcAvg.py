#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
DayL = ['mon','tue','wed','thu','fri','sat','sun']
date = DayL[datetime.datetime.today().weekday()] 
logname = "".join([date, ".log"])
logfile = open(logname, "r")
min = 100
max = 0
count = 0
sum = 0
for line in logfile:
  value = float(line)
  if value > max:
    max = value
  if value < min:
    min = value
  sum += value
  count += 1
# print(min)
# print(max)
# print(count)
avg = sum/count
# print(avg)
avgstr = '{:03.1f}'.format(avg)
# print(avgstr)
logfile.close()
command = "".join(["rm ",logname])
# print(command)
output = date + " min " + '{:.1f}'.format(min) 
output += " max " + '{:.1f}'.format(max) + " avg " + avgstr + '\n'
# print(output)
avgname = "".join([date, ".avg"])
avgfile = open(avgname, "w")
avgfile.write(output)
avgfile.close() 
os.system(command)

