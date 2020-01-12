#!/usr/bin/python
# -*- coding: utf-8 -*-

import email    # email procesing
import time	# for sleep
import os       # for work with filesystem
import MySQLdb as mdb

from datetime import datetime	# for debug output

# for random string :)
import random
import string

mail_path = '/var/mail/vhosts/kuvalda.lv/qwe/new/' # MAILBOX LOCATION
temp_path = "/home/svabis/web/utils/pdf_mail/temp/" # path to pdf

# ===============================================================
def mail_check():
    got_new_mail = False

    maillist = [] # array for emails

   # Fill picture Directory list array
    try:
        for filename in os.listdir(mail_path):
            maillist.append(filename)
    except:
        pass

   # Itterate picture Directory list array
    for filename in maillist:
       # READ MAIL FILE AS STRING
        with open (mail_path + filename, "r") as myfile:
            data = myfile.read()
           # DEFINE MAIL OBJECT
            b = email.message_from_string(data)
            if b.is_multipart():
               # ITERATE THROUGH MAIL PARTS
                for part in b.walk():
                    ctype = part.get_content_type()

                    print ctype

                    cdispo = str(part.get('Content-Disposition'))
                   # IF PART IS JPEG OR PNG OR APPLICATION(camera generated)-->
                    if ctype == 'application/pdf' or ctype == 'application/octet-stream':
                       # decode attachment
                        att = part.get_payload(decode=True)
# --> SAVE WITH ORIGINAL NAME
#                        with open(user_path + part.get_filename(), 'wb') as file:

# --> SAVE WITH RANDOMIZED NAME
                        with open(temp_path + str(b['Date']) + ''.join(random.choice(string.ascii_letters) for _ in range(3)) + '.PDF', 'wb') as file:
                             file.write( att )
                             got_new_mail = True
       # DELETE EMAIL FILE
        os.remove(mail_path + filename)
   # IF NEW MAIL IS COLLECTED --> return True
    return got_new_mail


#mail_check()
