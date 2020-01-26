# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import auth
#from django.core.context_processors import csrf

#from kamera.models import Kamera
from loginsys.models import User_data, User_kamera, Username_list
from django.contrib.auth.models import User     # autorisation library


# GET LIST FROM SQL USING PYTHON MYSQL CONNECTOR
def servermail_list(request):
   # Import mysql connector
    import MySQLdb as mdb
    con = mdb.connect('localhost', 'pastnieks', 'P@stn!eks', 'servermail');
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM virtual_users")
    result = []
   # Fill array with data from MySQL table
    for i in range(cur.rowcount):
        row = cur.fetchone()
        result.append(row[3])
    return sorted(result)



# !!!!! EXISTING USER LIST !!!!!
def existing_users(request):
    username = auth.get_user(request)
    args = {}
    args['username'] = username
    args['heading'] = u'Esošo lietotāju saraksts'

    if username.is_superuser:
        userlist = User.objects.all()
        args['userlist'] = userlist

        return render(request, 'user_list.html', args)
    return redirect ('/')


# !!!!! LIST EXISTING E-MAILS !!!!!
def list_emails(request):
    username = auth.get_user(request)
    args = {}
    args['username'] = username
    args['heading'] = u'Esošo e-pastu saraksts'

    if username.is_superuser:
        args['maillist'] = servermail_list(request)

        return render(request, 'email_list.html', args)
    return redirect ('/')
