# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect	# response to template, redirect to another view
from django.core.exceptions import ObjectDoesNotExist

from django.template.loader import get_template
from django.template import Context, RequestContext		# RequestContext <-- get user from request

from django.contrib.auth.models import User	# Django Users library
from django.contrib import auth			# autorisation library

from kamera.models import Kamera, Bilde # import models
from galerija.models import Galerija # import Galerija model

from main.paginator import Paginator	# import paginator
#from statistic.models import Ip_list, Ip_hit

# !!!!!
from kamera.views import kamera_main # cam_header, get_client_ip, det_domain, cam_header_type

#from django.core.context_processors import csrf

import math	# for rounding up Page Counter
import datetime
import os

from django.utils.timezone import localtime


# !!!!! Kamera TYPE CHOISE --> PUB, PRIV ===> MAIN VIEW !!!!!
def cam_sort_type(request, sort):
    if int(sort) < 1 or int(sort) > 3: # nelegal sort type--> 404
        return redirect ('kameras_main')
    response = redirect( '/cam/' )
# SET page_location COOKIE
    response.set_cookie( key='page_location', value='/cam/sort'+ str(sort) +'/' )
# SET cam_type COOKIE
    response.set_cookie( key='cam_type', value=str(sort) )
    return response


# !!!!!!! MAIN /kamera/ VIEW REDIRECT !!!!!
def cam_all(request):
    try:
        kamera1 = kamera_main.cam_objects(request)[0][0]
        kamera_slug = getattr( kamera1, 'kamera_slug' )	# get first kamera_slug from available Kamera object list depending on sort type
    except:
        args = kamera_main.cam_header(request)
        args['heading'] = u'Kamera nav atrasta'
        return render_to_response( 'no_cam.html', args  )
    return redirect( 'cam_id_grid', camid = kamera_slug, pageid = 1 )	# first argument is "name of the view (look in urls.py)", next are parameters


# !!!!!!! GRID VIEW !!!!!
def cam_id_grid(request, camid, pageid):
    if int(pageid) < 1:	# negative page number --> 404
        return redirect ('kameras_main')
    access = kamera_main.slug_access(request, camid) # test slug for access denied
    if access == False:
        return redirect ('kameras_main')

    kamera = Kamera.objects.get( kamera_slug = camid )

    bildes = Bilde.objects.filter( bilde_kamera_id = kamera )        # list of Bilde objects for current Kamera object

    img_on_page = 20
    pagecount = int(math.ceil( int(bildes.count()) / float( img_on_page )))    # integer identical to range by count

    if int(pageid) > pagecount and int(pageid) > 1:	# pageid exceeds pagecount --> last page
        if pagecount == 0:
            pageid = "1"
        else:
            pageid = str(pagecount)

    start_img = int(pageid) * img_on_page - img_on_page	# start from image NR
    end_img = int(pageid) * img_on_page			# end with image NR
    if end_img > bildes.count():	# if end NR exceeds limit set it to end NR
        end_img = bildes.count()

    args = kamera_main.cam_header(request)

   # ADD CSRF TOKEN
#    args.update(csrf(request))

    args['images'] = bildes.order_by('-bilde_datums')[start_img:end_img]	# -argument is for negative sort
    args['title'] = getattr( kamera, 'kamera_nos') + ' | ' + kamera_main.get_domain_full(request)	# return page title + kamera_nos + DOMAIN
    args['heading'] = u'Kamera:  ' + getattr( kamera, 'kamera_nos') + kamera_main.cam_header_type(kamera)
    args['active_tab'] = camid
    args['paginator'] = Paginator( pagecount, pageid )

   # IMAGE DELETE/SHARE OPTION
    try:
        usr = auth.get_user(request).username
        usr_del = User.objects.get(username = usr).k.filter(user=User.objects.get(username = usr)).get(kamera = kamera)
        args['owner'] = True
    except:
        pass

    response = render( request, 'grid.html', args)
# SET page_location COOKIE
    response.set_cookie( key='page_location', value='/cam/grid/'+ str(camid) +'/'+ str(pageid) +'/' )
    return response




# !!!!! GRID DELETE !!!!!
def grid_del(request, camid, pageid):
    if int(pageid) < 1: # negative page number --> 404
        return redirect ('kameras_main')
    access = kamera_main.slug_access(request, camid) # test slug for access denied
    if access == False:
        return redirect ('kameras_main')

    if request.POST:
        del_img = []
        for i in range (1,21):
            temp = request.POST.get('delete' + str(i), '') # get all checkbox data
            if temp != "":
                try: # if object does not exist
                    temp_bilde = Bilde.objects.get( bilde_thumb = temp[7:]) # REMOVE "/media/" from bilde_thumb name
                    del_img.append(temp_bilde)
                   # DELETE SOURCE FILE
                    try:
                        os.remove('/home/' + str(Kamera.objects.get(kamera_slug = camid).kamera_img_dir) + '/' + str(temp_bilde.bilde_nos))
                    except:
                        pass
                   # Delete Django object
                    temp_bilde.delete()
                except:
                    pass

    return redirect( 'cam_id_grid', camid = camid, pageid = pageid ) # Return to Grid View
