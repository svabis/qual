#!/usr/bin/python3.5

import os
import subprocess

output = subprocess.run(['ps', '-f', '-A'], stdout=subprocess.PIPE)
output = output.stdout.decode('utf-8')

proc = '/www/kuvalda/utils/mail_local.py'

if proc not in output:
    os.system( proc )
