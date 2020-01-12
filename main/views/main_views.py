# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect	# response to template, redirect to another view

from django.template import Context, RequestContext		# RequestContext <-- get user from request

from django.contrib.auth.models import User	# autorisation library
from django.contrib import auth			# autorisation library

#from statistic.models import  Ip_from
import datetime

#from django.core.context_processors import csrf


#import kamera.views.kamera_main as k # import page header/meta tags
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!         k parvietot uz main         !!!!!!
# !!!!!     k papildinat ar meta tagiem     !!!!!!
# !!!!!   k papildinat ar dinamisku title   !!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# SERVER ERROR 500
def handler500(request, *args, **argv):
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response


def errorpage(request):
    return render( request, '500.html')

# MAIN VIEW
def home(request):
#    args = k.cam_header(request) # Header (Tabs, e.t.c. from app kamera)
#    args['heading'] = u'Ievadiet PIN lai autorizētos, vai arī turpiniet standarta režīmā'
#    response = render( request, 'home.html', args )
    return redirect('/auth/pin/')
