# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import auth
#from django.core.context_processors import csrf

from django.contrib.auth.models import User # Django User models

import kamera.views.kamera_main as k # import page header/meta tags

from loginsys.models import User_pin # Pin code <-> User table

# !!!!! LOGIN USING PIN CODE
def pin(request):
   # if user is already authenticated --> redirect from here
    if request.user.is_authenticated():
        response = redirect('/gallery/')
        return response

    args = k.cam_header(request) # Header (Tabs, e.t.c. from app kamera)
#    args.update(csrf(request))      # encript data
    args['heading'] = "Autorizācija sistēmā izmantojot PIN kodu"

    if request.POST:
        pin = request.POST.get('pin', '') # usermname <= get variable from Form (name="username"), if not leave blank
        try:
            user = User_pin.objects.get( user_pin = pin ).user_user
        except:
            user = None

        if user is not None: # auth return None if this user does not exit, if not then:
            if user.is_active == False: # User is disabled in Django Admin -->
                args['login_error'] = "Lietotājs uz doto momentu ir bloķēts"
                return render(request, 'pin.html', args)

            user.backend = 'django.contrib.auth.backends.ModelBackend'
            auth.login( request, user )

            response = redirect('/gallery/')
            response.set_cookie( key='cam_type', value=2 )
            return response

        else: # if user does not exist:
            response = redirect('/gallery/')
            return response

    else: # actions if not request.POST (link clicked)
        return render(request, 'pin.html', args)


# !!!!! LOGIN
def login(request):
   # if user is already authenticated --> redirect from here
    if request.user.is_authenticated():
        response = redirect('/gallery/')
        return response

    args = k.cam_header(request) # Header (Tabs, e.t.c. from app kamera)
#    args.update(csrf(request))      # encript data
    args['heading'] = "Autorizācija sistēmā"

    if request.POST: # actions if login Form is submitted
        username = request.POST.get('username', '') # usermname <= get variable from Form (name="username"), if not leave blank
        password = request.POST.get('password', '') # password <= get variable from Form (name="password"), if not leave blank
        user = auth.authenticate( username = username, password = password ) # new variable --> user from auth system

        if user is not None: # auth return None if this user does not exit, if not then:
            if user.is_active == False: # User is disabled in Django Admin -->
                args['login_error'] = "Lietotājs uz doto momentu ir bloķēts"
                return render(request, 'login.html', args)
            auth.login( request, user ) # authorizate user from Form

            response = redirect('/gallery/')
            response.set_cookie( key='cam_type', value=3 )
            return response

        else: # if user does not exist:
            args['login_error']	= "Ievadīts lietotāja vārds vai parole nepareizi"
            return render(request, 'login.html', args)

    else: # actions if not request.POST (link clicked)
        return render(request, 'login.html', args)

# !!!!! LOG OUT
def logout(request):
    auth.logout(request)
    username = None

    response = redirect('/')
    response.delete_cookie('cam_type')
    try:
        response.delete_cookie('city')
    except:
        pass
    return response
