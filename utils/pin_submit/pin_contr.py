#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

from time import sleep
from datetime import datetime

import json # read control file
import threading # multiple proceses

# json_read thread (def control)
t1 = True

from pin_sub import pin_reader

def control():
  jsfile = "/www/kuvalda/static/cont/pin_container.json"
  stat = os.stat( jsfile ) # stat <-- file parameter object
  date = datetime.fromtimestamp( stat.st_ctime ) # file creation time

  while t1 == True:
    stat = os.stat( jsfile ) # stat <-- file parameter object
    c_date = datetime.fromtimestamp( stat.st_ctime ) # file creation time
    if c_date != date:
     # New Request
      date = c_date

     # Clear results
      f = open("/www/kuvalda/static/cont/pin_results.json","w")
      f.write("")
      f.close()

      if True:
#      try:
       # Load Command
        with open(jsfile) as f:
          data = json.load(f)

#          print data
         # Clear results
          f = open("/www/kuvalda/static/cont/pin_results.json","w")
          f.write("[]")
          f.close()

         # CLEAR DATA
          if data["data"] == "RESET":
            try:

# !!!!! CHANGE XLSX FILE LOCATION !!!!!
#              print
              os.system("rm /home/svabis/web/utils/pin_submit/pin_temp/*")

            except:
              pass
           # Procesing compleated
            f = open("/www/kuvalda/static/cont/pin_progress.json","w")
            f.write('{"progress": "100"}\r\n')
            f.close()
#            print "RESET - DONE"


         # PROCESS PIN
          if data["data"] == "PROCESS":
           # Procesing 0%
            f = open("/www/kuvalda/static/cont/pin_progress.json","w")
            f.write('{"progress": "0"}\r\n')
            f.close()
           # process PIN
            pin_reader()
            sleep(3)
           # Procesing compleated
            f = open("/www/kuvalda/static/cont/pin_progress.json","w")
            f.write('{"progress": "100"}\r\n')
            f.close()
#            print "END"

#      except:
#        print "ERROR OCURED"
#        pass
    sleep(3)


# =========================
json_read = threading.Thread( target = control )
json_read.start()

try:
  while True:
    sleep(10)

except (KeyboardInterrupt, SystemExit):
  print "\n"
 # Stop control thread
  t1 = False
  print "json read stoped"
  print "Aborting..."

