#!/usr/bin/python3.5

import os
import subprocess

from time import sleep

# Kill firefox, geckodriver & cont
try:
  os.system("killall -v firefox > /dev/null 2>&1 || true")
except:
  pass
sleep(5)

try:
  os.system("killall -v geckodriver > /dev/null 2>&1 || true")
except:
  pass
sleep(5)

try:
  os.system("killall -v pin_contr.py > /dev/null 2>&1 || true")
except:
  pass
sleep(5)


output = subprocess.run(['ps', '-f', '-A'], stdout=subprocess.PIPE)
output = output.stdout.decode('utf-8')

sleep(5)
#print (output);


proc = '/home/svabis/web/utils/pin_submit/pin_contr.py'

if proc not in output:
    os.system( proc )
