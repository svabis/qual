# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect	# response to template, redirect to another view
from django.core.exceptions import ObjectDoesNotExist

from django.template import Context, RequestContext		# RequestContext <-- get user from request

from django.contrib.auth.models import User	# Django Users library
from django.contrib import auth			# autorisation library

from kamera.models import Kamera, Bilde # import models
from galerija.models import Galerija # import Galerija model
from django.core.files import File # for SHARE TO Galerija

# !!!!!
from kamera.views import kamera_main # cam_header, get_client_ip, det_domain, cam_header_type

import math	# for rounding up Page Counter
import datetime
import os


# !!!!!!! FULSIZE IMAGE VIEW
def bilde_id(request, pageid, imgid, show='', date=''):
    try:
        if date:
            imgname = date + '/' + imgid + '.jpg'
        else:
            imgname = imgid + '.jpg'
        bilde = Bilde.objects.get( bilde_bilde = imgname ) # get image to display
    except ObjectDoesNotExist:	# not existing bilde --> 404
        return redirect ('kameras_main')
    if int(pageid) < 1: # negative page number --> 404
        return redirect ('kameras_main')

    return_cam = getattr( bilde, 'bilde_kamera_id') # get bilde_kamera_id to return to
    bildes = Bilde.objects.filter( bilde_kamera_id = return_cam ).order_by('-bilde_datums')	# filtered list of Bilde objects
#    bildes = Bilde.objects.filter( bilde_kamera_id = return_cam )        # list of Bilde objects for current Kamera object
    img_on_page = 20
    pagecount = int(math.ceil( int(bildes.count()) / float( img_on_page )))    # integer identical to range by count
    if int(pageid) > pagecount: # pageid exceeds pagecount --> 404
        return redirect ('kameras_main')

    args = kamera_main.cam_header(request)
    args['image'] = bilde
    args['time'] = bilde.bilde_datums
    args['title'] = getattr( return_cam, 'kamera_nos') + ' | ' + kamera_main.get_domain_full(request)   # return page title + kamera_nos + DOMAIN
    args['heading'] = u'Kamera:  ' + getattr( return_cam, 'kamera_nos') + kamera_main.cam_header_type(return_cam)
    args['active_tab'] = getattr( return_cam, 'kamera_slug') # get kamera_slug

# Getting Next and Previous Bilde objects from filtered list
    counter = 0 # set iteration counter
    for img in bildes:
        if img == bilde:	# if image from this iteration == curent image do:
            try:	# try is for if previous does not exist
                args['back_img'] = getattr( bildes[counter - 1], 'bilde_bilde').name  # get next object 'bilde_bilde' filename
            except:
                pass
            try:	# try is for if next does not exist
                args['next_img'] = getattr( bildes[counter + 1], 'bilde_bilde').name  # get next object 'bilde_bilde' filename
            except:
                pass
            return_page = ( counter / 20 ) + 1	# locates page number you ar at the moment
        counter += 1	# increase iteration counter
    args['back_page'] = return_page

    if show != '':
        args['slideshow'] = True

   # IMAGE DELETE/SHARE OPTION
    try:
        usr = auth.get_user(request).username
        usr_del = User.objects.get(username = usr).k.filter(user=User.objects.get(username = usr)).get(kamera = return_cam)
        args['img_owner'] = True
    except:
        pass
#        args['img_owner'] = return_cam

    response = render( request, 'image.html', args)
# SET page_location COOKIE
    response.set_cookie( key='page_location', value='/cam/img/'+ str(pageid) +'/'+ str(imgid) +'/' )
    return response

# ==========================
# !!!!! BILDE DELETE !!!!!!
def bilde_del(request, pageid, del_id, date=''):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/")

    if date != '':
        del_id = date + '/' + del_id

    try:
        image = Bilde.objects.get( bilde_bilde = (del_id + '.jpg'))
        kamera_slug = Kamera.objects.get(id = image.bilde_kamera_id_id).kamera_slug
       # DELETE SOURCE FILE
        try:
            os.remove('/home/' + str(Kamera.objects.get(id = image.bilde_kamera_id_id).kamera_img_dir) + '/' + str(image.bilde_nos))
        except:
            pass
       # DELETE IMAGE FROM Django DATABASE
        image.delete()

    except ObjectDoesNotExist:
        return redirect ('kameras_main')
    return redirect( 'cam_id_grid', camid = str(kamera_slug), pageid = pageid )


# !!!!! BILDE SHARE TO GALERIJA
def share(request, pageid, shareid, date=''):
    if auth.get_user(request).get_username() == '': # IF NO USER -->
        return redirect ("/")

    if date != '':
        shareid = date + '/' + shareid

    try:
       # Existing image
        image = Bilde.objects.get( bilde_bilde = (shareid + '.jpg'))
       # get slug for redirect after share
        kamera_slug = Kamera.objects.get(id = image.bilde_kamera_id_id).kamera_slug
       # create new object
        obj = Galerija( bilde_nos = image.bilde_nos,
                        bilde_bilde = File(image.bilde_bilde, image.bilde_bilde.name),  # THIS IS THE TRICK FOR COPYING FILES
                        bilde_thumb = File(image.bilde_thumb, image.bilde_thumb.name),  # THIS IS THE TRICK FOR COPYING FILES
                        bilde_datums = image.bilde_datums)
        obj.save() # save new object Galerija into database

    except ObjectDoesNotExist:
        return redirect ('kameras_main')
    return redirect( 'cam_id_grid', camid = str(kamera_slug), pageid = pageid )


#=========================================================================================

# !!!!!!! IMAGE LIKE CLICK FUNCTION
'''
def bilde_like(request, pageid, likeid):
    try:
        image = Bilde.objects.get( bilde_bilde = (likeid + '.jpg'))
        image.bilde_patik += 1
        image.save()
    except ObjectDoesNotExist:
        return redirect ('kameras_main')
    return redirect( 'bilde_id', pageid = pageid, bildeid = likeid )  #  first argument is "name of the view (look in urls.py)", next are parameters
'''
