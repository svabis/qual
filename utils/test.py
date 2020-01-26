#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import imaplib
import getpass
import email
import datetime

import time
import os

# for random string :)
import random
import string


# =======================================+== Update MySQL entry ===============================================
def update_sql_entry(id, time):
    import MySQLdb as mdb
    con = mdb.connect('localhost', 'kuvalda_web', 'kuv@ld@_WEB!', 'kuvalda_db');

    cursor = con.cursor()
    cursor.execute("UPDATE user_data SET user_last_mail_check=%s WHERE id=%s", (time, id))
    con.commit()
    con.close()


# =========================================== get data rom MySQL ===============================================
def user_cam_data():
    import MySQLdb as mdb

   # USER_DATA
    user_data = []
    con = mdb.connect('localhost', 'kuvalda_web', 'kuv@ld@_WEB!', 'kuvalda_db');
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM user_data")
    for i in range(cur.rowcount):
        row = cur.fetchone()
        if row[3] == 1:
            user_data.append([row[2],row[4],row[5],row[0]])
#            print row
#    print user_data
#    print

   # AUTH_USER
    auth_user = []
    con = mdb.connect('localhost', 'kuvalda_web', 'kuv@ld@_WEB!', 'kuvalda_db');
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM auth_user")
    for i in range(cur.rowcount):
        row = cur.fetchone()
        auth_user.append([row[0],row[4]])

    temp_array = []
    for n1 in user_data:
        for n2 in auth_user:
            if n1[0] == n2[0]:
                temp_array.append([n1[0],n1[1],n2[1],n1[2],n1[3]])
#    print temp_array
#    print
    user_data = temp_array # temporay array --> user_data

   # USER_KAMERAS
    user_kameras = []
    con = mdb.connect('localhost', 'kuvalda_web', 'kuv@ld@_WEB!', 'kuvalda_db');
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM user_kameras")
    for i in range(cur.rowcount):
        row = cur.fetchone()
        user_kameras.append([row[2],row[1]])

    temp_array = []
    for n1 in user_data:
        for n2 in user_kameras:
            if n1[0] == n2[0]:
                temp_array.append([n2[1],n1[1],n1[2],n1[3],n1[4]])
#    print temp_array
#    print
    user_data = temp_array # temporay array --> user_data

   # KAMERAS
    cam = []
    con = mdb.connect('localhost', 'kuvalda_web', 'kuv@ld@_WEB!', 'kuvalda_db');
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM kameras")
    for i in range(cur.rowcount):
        row = cur.fetchone()
        cam.append([row[0],row[4]])

    temp_array = []
    for n1 in user_data:
        for n2 in cam:
            if n1[0] == n2[0]:
                temp_array.append([n2[1],n1[1],n1[2], n1[3],n1[4]])
#    print temp_array
#    print
    user_data = temp_array # temporay array --> user_data
    return user_data

# ============================================ Process Mailbox ==============================================

# Function that processess the 'M' mailbox
def process_mailbox(M, file_path, last_date):
  # rv - 'OK'	# data - ['1 2 3']	# data[0] - '1 2 3'	# data[0].split() - 1,2,3
  rv, data = M.search(None, "ALL")
  if rv != 'OK':
      print "No messages found!"
      return

# get last DateTime
  count = 0 # counter or only last e-mail
  new_date = last_date # set "empty" new_data
  new_img = False # set to False, if True --> run script for image insert into Django

  for num in reversed(data[0].split()):
      rv, data = M.fetch(num, '(RFC822)')
      if rv != 'OK':
          print "ERROR getting message", num
          return

     # Define e-mail as msg variable
      msg = email.message_from_string(data[0][1])

     # Extract Date from email
      date_tuple = email.utils.parsedate_tz(msg['Date'])
     # convert time to local_date variable if provided
      if date_tuple:
          local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))

      if count == 0: # set new_date to last processed e-mail DateTime
          new_date = local_date
          count += 1

# !!!!!!!!!! INSERT BRAIN HERE !!!!!!!!!!
      if local_date <= last_date: # if this mail is older than the last checked --> stop
          return [new_date, new_img]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

      if msg.is_multipart(): # if mail is multipart --> extract Attachment
          name = ( ( msg['Date'].replace('(', ' ') ).replace(')', ' ') ).replace(',', ' ').replace(' ', '-')
          for part in msg.walk():
              ctype = part.get_content_type()
#              print ctype
              cdispo = str(part.get('Content-Disposition', None))
              if cdispo:
                  dispositions = cdispo.strip().split(";");
                  if bool(cdispo and dispositions[0].lower() == "attachment"):

                     # CAMERA NATIVE IMG FORMAT
                      if ctype == 'application/octet-stream':
                          att = part.get_payload(decode=True)  # decode
#                          with open(file_path + str(part.get_filename()), 'wb') as file:
                          with open(file_path + str(name) + ''.join(random.choice(string.ascii_letters) for _ in range(3)) + '.JPG', 'wb') as file:
                             file.write( att )
                             print msg['Date']
                             new_img = True

#            # ANY JPEG or PNG image (for test using send mail with image attached)
              if ctype == 'image/jpeg': # or ctype == 'image/png' or ctype == 'application/octet-stream':    # IF PART IS JP$
                  att = part.get_payload(decode=True)  # decode
                  with open(file_path + str(name) + ''.join(random.choice(string.ascii_letters) for _ in range(3)) + '.JPG', 'wb') as file:
                      file.write( att )
                      print msg['Date']
                      new_img = True

  return [new_date, new_img]

# ============================================================================================

# d = ('API/0000', datetime.datetime(2017, 7, 17, 20, 44, 52), 'kuiliskur@gmail.com', 'mezakuilis', '28L')

# Main function for mail check
def check_mail(d):

   # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   # !!! imap server need to be in user_data !!!
   # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    M = imaplib.IMAP4_SSL('imap.gmail.com') # imap server

    try:
#        M.login('kuiliskur@gmail.com', 'mezakuilis')
        M.login(d[2], d[3])
    except imaplib.IMAP4.error:
        print "LOGIN FAILED!!! "
        return [d[1], False]

#    rv, mailboxes = M.list()
#    rv, data = M.select( mailboxes[0].split()[2] ) # two lines result - the same

    rv, data = M.select("INBOX") # two lines result - the same
    if rv == 'OK':
#        print 'procesing'
        d = process_mailbox( M, str('/home/'+ d[0] +'/'), d[1] )
        M.close()
    M.logout()
    return d

# ==================================================================================

# MAIN
# Delay on script run
#time.sleep(60)

while True:
#if True:
    user_data = user_cam_data()
#    print user_data
   # convert Time
    for d in user_data:
        d[1] = d[1] + datetime.timedelta(hours=3)
#        print d

    for d in user_data: # iterate all user_data entries
#            d = user_data[2]

            print d
