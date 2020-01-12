#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

from time import sleep
from datetime import datetime

import json # read control file
from StringIO import StringIO # read array from file
import threading # multiple proceses

from cma import cma_search
from maersk import maersk_search
from hapag import hapag_search
from msc import msc_search


jsfile = "/www/kuvalda/static/container.json"
stat = os.stat( jsfile ) # stat <-- file parameter object
date = datetime.fromtimestamp( stat.st_ctime ) # file creation time

try:
  while True:
    stat = os.stat( jsfile ) # stat <-- file parameter object
    c_date = datetime.fromtimestamp( stat.st_ctime ) # file creation time
    if c_date != date:
     # New Search Request
      date = c_date

     # Clear results
      f = open("/www/kuvalda/static/results.json","w+")
      f.write("")
      f.close()

      try:
       # Load Search data
        infile = "/www/kuvalda/static/container.json"
        lines = [line.rstrip('\n') for line in open(infile)]
        with open(infile) as f:
          data = json.load(f)
          search = re.findall("(\w{4}\d{7})", data["data"])
          if len(search) != 0:
           # Stop current search thread
            try:
              cont_search.stop()
              os.system("killall -v firefox > /dev/null 2>&1 || true")
              os.system("killall -v geckodriver > /dev/null 2>&1 || true")
              sleep(0.2)
            except:
              pass

            progress = False

           # CMA
            if data["company"] == "cma":
              print "cma"
              progress = True
              cont_search = threading.Thread( target=cma_search, args=[search] )
              cont_search.start()

           # MAERSK
            if data["company"] == "maersk":
              print "maersk"
              progress = True
              cont_search = threading.Thread( target=maersk_search, args=[search] )
              cont_search.start()

           # HAPAG-LLOYD
            if data["company"] == "hapag":
              print "hapag"
              progress = True
              cont_search = threading.Thread( target=hapag_search, args=[search] )
              cont_search.start()

           # MSC
            if data["company"] == "msc":
              print "msc"
              progress = True
              cont_search = threading.Thread( target=msc_search, args=[search] )
              cont_search.start()

            while progress:
           # Get curent result count
              infile = "/www/kuvalda/static/results.json"
              lines = [line.rstrip('\n') for line in open(infile)]
              if len(lines) == 0:
                rez = 0
              else:
                rez = len( str(lines).split("],") )

              if rez == len(search):
                progress = False

             # Update progress-bar
              f = open("/www/kuvalda/static/progress.json","w+")
              f.write('{"progress": "' + str( int( float( rez ) / float( len(search) ) * 100 ) ) + '"}\r\n')
              f.close()
              sleep(0.2)

      except:
       # Error, something went wrong
       # Stop current search thread
        try:
          cont_search.stop()
          os.system("killall -v firefox > /dev/null 2>&1 || true")
          os.system("killall -v geckodriver > /dev/null 2>&1 || true")
          sleep(0.2)
        except:
          pass
        print "JSON ERROR"

    sleep(0.5)

except (KeyboardInterrupt, SystemExit):
  print "\nAborting..."

