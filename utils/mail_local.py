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

# ===============================================================
mail_location = '/var/mail/vhosts/kuvalda.lv/' # MAILBOX LOCATION
kamera = []

def sql_read():
    con = mdb.connect('localhost', 'kuvalda_web', 'kuv@ld@_WEB!', 'kuvalda_db');
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM kameras")

    rezult = []
# Fill array with data from MySQL table
    for i in range(cur.rowcount):
        row = cur.fetchone()
        cam = []
        cam.append(row[4]) # django --> kamera_img_dir
        cam.append(row[5]) # django --> kamera_email
        rezult.append(cam)
    return rezult

# ===============================================================
def mail_check(cam):
    got_new_mail = False

   # If Kamera objecta has email field filled --> continue
    if cam[1] != '':
        user_path = "/home/" + cam[0] + "/" # path to images
        path = mail_location + cam[1] + '/new/' # PATH TO NEW MAIL FOLDER FOR CAMERA
        maillist = [] # array for emails

       # Fill picture Directory list array
        try:
            for filename in os.listdir(path):
                maillist.append(filename)
        except:
            pass

       # Itterate picture Directory list array
        for filename in maillist:
           # READ MAIL FILE AS STRING
            with open (path + filename, "r") as myfile:
                data = myfile.read()
               # DEFINE MAIL OBJECT
                b = email.message_from_string(data)
                if b.is_multipart():
                   # ITERATE THROUGH MAIL PARTS
                    for part in b.walk():
                        ctype = part.get_content_type()
                        cdispo = str(part.get('Content-Disposition'))
                       # IF PART IS JPEG OR PNG OR APPLICATION(camera generated)-->
                        if ctype == 'image/jpeg' or ctype == 'image/png' or ctype == 'application/octet-stream':
                           # decode attachment
                            att = part.get_payload(decode=True)
# --> SAVE WITH ORIGINAL NAME IN CAMERA DIR
#                            with open(user_path + part.get_filename(), 'wb') as file:
                            with open(user_path + str(b['Date']) + ''.join(random.choice(string.ascii_letters) for _ in range(3)) + '.JPG', 'wb') as file:
                                file.write( att )
                                got_new_mail = True
               # DELETE EMAIL FILE
                os.remove(path + filename)
   # IF NEW MAIL IS COLLECTED --> return True
    return got_new_mail


# ===============================================================
if __name__ == '__main__':
    time.sleep(60)
    while True:
        kamera = sql_read()
       # CYCLE BEFORE RETEST SQL
        for _ in range(0,200):
           # ITERATION THROUG CAMERA ARRAY
            for k in kamera:
                if mail_check(k) == True:

                    if k[1] == "app":
                      os.system("cp /home/API/0013/* /home/AI/")

                    t = datetime.now()
                    os.system("/www/kuvalda/utils/img_refresh.py")
            time.sleep(1)

