#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
#import sendSMS
import sendStatus
import turnSteps

def stelleHeizung(stufe):
  hfile = open("/home/mabe42/heizungsStufe", "r")
  alteStufe = int(hfile.read())
  print "Alte Stufe " + str(alteStufe) + " - Neue Stufe " + str(stufe)
  hfile.close()
  hfile = open("/home/mabe42/heizungsStufe", "w")
  hfile.write(stufe)
  hfile.close()
  turnSteps.main((int(stufe)-alteStufe)*50)
  
#smsClass = os.environ['SMS_1_CLASS']
smsSender = os.environ['SMS_1_NUMBER']
smsText = os.environ['SMS_1_TEXT']

lfile = open("/home/mabe42/smslogfile.log", "a")
#lfile.write("received SMS:\nClass: " + smsClass)
lfile.write("Sender: "  + smsSender)
lfile.write(" Text: " + smsText)

words = smsText.split()

if (words[0] == "Reboot"):
  lfile.write("\n - SMS requested reboot\n")
  os.system("sudo reboot -n")
elif (words[0] == "Status"):
  lfile.write("\n - SMS requested status message\n")
  sendStatus.main()
elif (words[0] == "Restsms"):
  lfile.write("\n - SMS sent new number of available SMSs\n")
  sfile = open("/home/mabe42/restsms", "w")
  sfile.write(words[1])
  sfile.close()
elif (words[0] == "Stufe"):
  lfile.write("\n - Neue Stufe der Heizung: " + words[1] + "\n")
  stelleHeizung(words[1])
else:
  lfile.write("\n - unknown command from SMS - forwarding to default number\n")
  cfile = open("/home/matthias/content", "w")
  cfile.write(smsText)
  cfile.close()

lfile.close()

