#!/usr/bin/python
# -*- coding: utf-8 -*-
import email    # email procesing
import time
import os       # for work with filesystem
import MySQLdb as mdb

# Delay on script run
time.sleep(60)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #
# IN FUTURE DO NOT PROCESS E-MAILS NEWER THAN 1 WEAK #
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! #

while True:
#if True:

    con = mdb.connect('localhost', 'kuvalda_web', 'kuv@ld@_WEB!', 'kuvalda_db');
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM kameras")

    kamera = []
# Fill Kamera array with data from MySQL table
    for i in range(cur.rowcount):
        row = cur.fetchone()
#        print row[0], row[4], row[5]
        cam = []
        cam.append(row[4]) # django --> kamera_img_dir
        cam.append(row[5]) # django --> kamera_email
        kamera.append(cam)

        mail_location = '/var/mail/vhosts/kuvalda.lv/' # MAILBOX LOCATION
# Iterate trough Kamera object
        for cam in kamera:
# If Kamera objecta has email field filled --> continue
            if cam[1] != '':
#		print cam[0]
                user_path = "/home/" + cam[0] + "/" # path to images
                path = mail_location + cam[1] + '/new/' # PATH TO NEW MAIL FOLDER FOR CAMERA
                maillist = [] # array for emails
# Fill picture Directory list array
                try:
                    for filename in os.listdir(path):
                        maillist.append(filename)
                except:
                    pass
# EACH INBOX MAIL
                for filename in maillist:
# READ MAIL FILE AS STRING
                    with open (path + filename, "r") as myfile:
                        data = myfile.read()
# DEFINE MAIL OBJECT
                        b = email.message_from_string(data)
                        if b.is_multipart():
#                            print "multipart"
                            for part in b.walk():   # ITERATE THROUGH MAIL PARTS
                                ctype = part.get_content_type()
                                cdispo = str(part.get('Content-Disposition'))
#                                print ctype
                                if ctype == 'image/jpeg' or ctype == 'image/png' or ctype == 'application/octet-stream':    # IF PART IS JPEG OR PNG -->
#                                    print "if ..........."
                                    att = part.get_payload(decode=True)  # decode
                                    with open(user_path + part.get_filename(), 'wb') as file:     # --> SAVE WITH ORIGINAL NAME IN CAMERA DIR
                                        file.write( att )
# !!! DONT NEED THIS PART !!!
# not multipart - i.e. plain text, no attachments, keeping fingers crossed
                        else:
#                            print "single"
                            pass
                    os.remove(path + filename)  # DELETE EMAIL FILE
    time.sleep(10)


