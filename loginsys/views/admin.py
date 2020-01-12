# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import auth
#from django.core.context_processors import csrf

#from kamera.models import Kamera
from loginsys.models import User_data, User_kamera, Username_list
from django.contrib.auth.models import User     # autorisation library

#from loginsys import mail

#import datetime, pytz
#import textwrap
#import os


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

