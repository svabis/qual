#!/usr/bin/python

import os
import time

import commands
output = commands.getoutput('ps -f -A')

proc = '/www/kuvalda/manage.py refresh'

while proc in output:
    output = commands.getoutput('ps -f -A')
    time.sleep(1)

os.system("/www/kuvalda/manage.py refresh")
