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

from mail_read import mail_check
from pdf_read import pdf_process

def control():
  jsfile = "/www/kuvalda/static/cont/pdf_container.json"
  stat = os.stat( jsfile ) # stat <-- file parameter object
  date = datetime.fromtimestamp( stat.st_ctime ) # file creation time

  while t1 == True:
    stat = os.stat( jsfile ) # stat <-- file parameter object
    c_date = datetime.fromtimestamp( stat.st_ctime ) # file creation time
    if c_date != date:
     # New Request
      date = c_date

     # Clear results
      f = open("/www/kuvalda/static/cont/pdf_results.json","w")
      f.write("")
      f.close()

      try:
       # Load Command
        with open(jsfile) as f:
          data = json.load(f)

          print data
         # Clear results
          f = open("/www/kuvalda/static/cont/pdf_results.json","w")
          f.write("[]")
          f.close()

         # CLEAR DATA
          if data["data"] == "RESET":
           # Delete saved e-mails from temp older
            try:
              os.system("rm /home/svabis/web/utils/pdf_mail/temp/*")
            except:
              pass
           # Procesing compleated
            f = open("/www/kuvalda/static/cont/pdf_progress.json","w")
            f.write('{"progress": "100"}\r\n')
            f.close()
            print "RESET - DONE"

         # PROCESS PDF
          if data["data"] == "PROCESS":
           # Procesing 0%
            f = open("/www/kuvalda/static/cont/pdf_progress.json","w")
            f.write('{"progress": "0"}\r\n')
            f.close()
           # read PDF files from inbox
            mail_check()
           # process PDF
            pdf_process()

            sleep(3)
           # Procesing compleated
            f = open("/www/kuvalda/static/cont/pdf_progress.json","w")
            f.write('{"progress": "100"}\r\n')
            f.close()
            print "END"

      except:
        print "ERROR OCURED"
        pass
    sleep(5)


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

