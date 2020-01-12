#!/usr/bin/python2
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User	# autorisation library
from django.contrib import auth			# autorisation library
from kamera.models import Kamera, Bilde # import aplication models

import math	# for rounding up Page Counter
import datetime
import calendar
import os

# !!!!! DST !!!!!
def dst(img_date):
    today = img_date.date()
    year = today.year

    dst_start = max(week[-1] for week in calendar.monthcalendar(year, 10)) # last sunday of this years Oct
    dst_end   = max(week[-1] for week in calendar.monthcalendar(year, 3))  # last sunday of this years Mar
   # convert to date objects
    date_dst_start = datetime.date(year, 10, dst_start)
    date_dst_end = datetime.date(year, 3, dst_end)
   # compare if in range (summer --> True)
    if date_dst_end <= today <= date_dst_start:
        return 1
    else:
        return 0

# !!!!! Kamera object return to views using sort by PUB, PRIV, ///SHARE///
def cam_objects(request):
    if str('cam_type') in request.COOKIES:
#        if request.COOKIES.get('cam_type') == '1':
#            return kamera_sort[1](request)      # PUBLIC (DEFAULT VALUE)
        if request.COOKIES.get('cam_type') == '2':
            return kamera_sort[2](request)      # PRIVATE
        if request.COOKIES.get('cam_type') == '3':
            return kamera_sort[3](request)      # PUBLIC + PRIVATE
    else:
        return kamera_sort[3](request)      # DEFAULT VALUE

# !!!!!!! IP GRABBER
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

# !!!!! DOMAIN short / full (UPPERCASE)
def get_domain(request):
    domain = request.META['HTTP_HOST'].split('.')[-1]
    return domain

def get_domain_full(request):
#    domain = request.META['HTTP_HOST'].upper() # OUTPUT ==> WWW.KUVALDA.LV
    dot = str( get_domain(request) )
    if dot == 'lv':
        domain = 'Kuvalda.lv'
    else:
        domain = 'TrailCamPhoto.' + dot         # OUTPUT ==> TrailCamPhoto.<xx>
    return domain



# !!!!!!! MAIN ARGUMENT DEFINITION
def cam_header(request):
    args = {}
    kameras = cam_objects(request)	# Kamera objects depending on sort type
    args['kameras'] = kameras
    args['title'] = get_domain_full(request)
    args['username'] = auth.get_user(request)	# returns User model --> .username is <username> variable
    args['ip'] = get_client_ip(request)	# gets IP, and adds it to statistics models
    args['domain'] = get_domain(request)
    args['full_domain'] = args['title']

    try:
        if str('cam_type') in request.COOKIES:
            args['cam_sort'] = int(request.COOKIES.get('cam_type'))
    except:
            pass
#            args['cam_sort'] = int(request.COOKIES.get('cam_type'))
    return args

# PUB, PRIV, SHARE --> string
def cam_header_type(kamera):
    type_str_mod = getattr( kamera, 'kamera_type')      # PUB, PRIV, SHARE
    if type_str_mod == 'PUB':
        type_str = u' (publiska)'
    if type_str_mod == 'PRIV':
        type_str = u' (privāta)'
#    if type_str_mod == 'SEC':
#        type_str = u' (apsardzes)'
    return type_str






# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! SORT START !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!! Kamera OBJECT CHOISES: PUBLIC, PRIVATE, e.t.c.
def sort1(request):	# RETURN PUBLIC
    cam_pub = Kamera.objects.filter(kamera_type='PUB').order_by('id')
    cam_obj = []
    for cam in cam_pub:
        cam_obj.append( [cam, "PUB"] )
    return cam_obj

def sort2(request):	# RETURN PRIVATE Kamera
    try:
        usr = auth.get_user(request).username
        cam_obj = []

        usr_cam_obj = User.objects.get(username = usr).k.filter(user=User.objects.get(username = usr)) # --> User_kamera object's
        for cam in usr_cam_obj:
            cam_obj.append( [cam.kamera, "PRIV"] )

    except:
        cam_obj = []
        cam_pub = Kamera.objects.filter(kamera_type='PUB').order_by('id')
	for cam in cam_pub:
            cam_obj.append( [cam, "PUB"] )
    return cam_obj

def sort3(request):	# RETURN PUBLIC + PRIVATE Kamera
    try:
        usr = auth.get_user(request).username
        cam_obj = []

        usr_cam_obj = User.objects.get(username = usr).k.filter(user=User.objects.get(username = usr)) # --> User_kamera object's
        for cam in usr_cam_obj:
            cam_obj.append( [cam.kamera, "PRIV"] )

        cam_pub = Kamera.objects.all().filter(kamera_type='PUB').order_by('id')
	for cam in cam_pub:
            if [cam, "PRIV"] not in cam_obj: # NO DUBLICATES
                cam_obj.append( [cam, "PUB"] )

    except: # if no User kameras --> Return only PUBLIC
        cam_obj = []
        cam_pub = Kamera.objects.filter(kamera_type='PUB').order_by('id')
	for cam in cam_pub:
            cam_obj.append( [cam, "PUB"] )
    return cam_obj
#    user = str(Kamera.objects.all()[3].user_kamera_set.get( kamera =Kamera.objects.all()[3] ).user.user_user)
kamera_sort = {1 : sort1, 2 : sort2, 3 : sort3, }



# !!!!! Kamera.kamera_slug ACCESS DENIED/GRANTED
def slug_access(request, slug):     # RETURN PUBLIC + PRIVATE Kamera.kamera_slug list
    cam = sort3(request)
    t = 0 # cycle count
    f = 0 # error count
    for c in cam:
        if c[0].kamera_slug != slug:
            f += 1
        t += 1
    if t == f:	# no slug found -->ACCESS DENIED
        return False
    return True # ACCESS GRANTED
