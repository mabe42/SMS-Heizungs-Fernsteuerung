#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
  import datetime
  import os
  import subprocess
  import time
# the sensor id needs to be adapted to that of the sensor present
  tfile = open("/sys/bus/w1/devices/10-000802e75cf1/w1_slave")
  text = tfile.read()
  tfile.close()
  temperature_data = text.split()[-1]
  temperature = float(temperature_data[2:])
  temperature = temperature / 1000
#  temperature = 21.8123

#  output = "\""
  output = subprocess.check_output("date", shell=True)
  output += subprocess.check_output("uptime", shell=True)

  output = output + "now " + '{:03.1f}'.format(temperature)
#  print(output)
# echo "test2f" | gammu-smsd-inject TEXT "+4917651012493"
  cfile = open("/home/mabe42/content", "w")
  cfile.write(output)
  cfile.close()
  lfile = open("/home/mabe42/smslogfile.log", "a")
  lfile.write("sendStatus.py wrote content\n")
  lfile.close

if __name__ == "__main__":
  main()

