#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def main(nr):
  import datetime
  import os
  import subprocess
  import time

  if os.path.isfile("/home/mabe42/content"):
    lfile = open("/home/mabe42/smslogfile.log", "a")

    hfile = open("/home/mabe42/heizungsStufe")
    stufe = hfile.read()
    hfile.close()
    sfile = open("/home/mabe42/restsms")
    sms = sfile.read()
    sfile.close()
    smscount = int(sms)
    smscount -= 1
    sms = str(smscount)

    cfile = open("/home/mabe42/content")
    text = cfile.read()
    cfile.close()

    output = text + " r: " + sms + " s: " + stufe
    if (len(nr) == 0) :
      nr = "+491234567890" # you need to put the correct phone number

# echo "my message" | gammu-smsd-inject TEXT "+491234567890"
    command = "echo " + "\"" + output
    command = command + "\" | gammu-smsd-inject TEXT \"" + nr + "\""
#    print(command)
    sfile = open("/home/mabe42/restsms", "w")
    sfile.write(sms)
    sfile.close()
    time.sleep(60)
    os.system(command)
#temp = subprocess.check_output(command, shell=True)
    lfile.write("sendSMS.py to " + nr + "\n")
    lfile.close
    os.system("rm /home/mabe42/content")

if __name__ == "__main__":
  if (len(sys.argv) < 2):
    main("")
  else:
    main(sys.argv[1])

