#!/usr/bin/python
# -*- coding: utf-8 -*-
#import email    # email procesing
#import time
#import os       # for work with filesystem
import MySQLdb as mdb
from random import randint


def get_used_mail():
#    con = mdb.connect('localhost', 'root', 'Reinisisthebest', 'servermail');
    con = mdb.connect('localhost', 'kuvalda_pasts', 'Reinisisthebest', 'servermail');
    with con:
        cur = con.cursor()
#        cur.execute("INSERT INTO virtual_users ( `domain_id`, `password` , `email`) VALUES ( '1', ENCRYPT('#ParoleCam1!', CONCAT('$6$', SUBSTRING(SHA(RAND()), -16))), 'lv0022@kuvalda.lv');")
#        cur.execute("INSERT INTO virtual_users ( `domain_id`, `password` , `email`) VALUES ( '1', '$6$aiubxcahbjHVAYSVUCH', 'lv0021@kuvalda.lv');")
#        cur.execute("DELETE FROM virtual_users WHERE email='lv0021@kuvalda.lv';")
        cur.execute("SELECT * FROM virtual_users")

    used_mail = []
    for i in range(cur.rowcount):
        row = cur.fetchone()
        if row[3].startswith('lv'):
            used_mail.append(row[3].split('@')[0])
    return used_mail

def create_new_mail(mail):
#    con = mdb.connect('localhost', 'root', 'Reinisisthebest', 'servermail');
    con = mdb.connect('localhost', 'kuvalda_pasts', 'Reinisisthebest', 'servermail');
    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO virtual_users ( `domain_id`, `password` , `email`) VALUES ( '1', '$6$aiubxcahbjHVAYSVUCH', '" + mail +  "@kuvalda.lv');")
#        cur.execute("DELETE FROM virtual_users WHERE email='lv0021@kuvalda.lv';")
#        cur.execute("SELECT * FROM virtual_users")

def generate_mail():
    used_mail = get_used_mail()
    new = ''.join(str(randint(0,9)) for _ in range(4))
    if 'lv' + new not in used_mail:
        new_mail = []
        new_mail.append('lv' + new)
        new_mail.append('LV/' + new)
        create_new_mail('lv' + new)
        return new_mail
    else:
        generate_mail()

#used_mail =  get_used_mail()
#new = generate_mail()

#for _ in range (0,10000):
#    new = generate_mail()
#    if new == None:
#        print "ERROR"


