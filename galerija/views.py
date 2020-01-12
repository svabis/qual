# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect # response to template, redirect to another view
from django.core.exceptions import ObjectDoesNotExist

from django.template.loader import get_template
from django.template import Context, RequestContext             # RequestContext <-- get user from request

from django.contrib.auth.models import User     # Django Users library
from django.contrib import auth                 # autorisation library

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!         k parvietot uz main         !!!!!!
# !!!!!     k papildinat ar meta tagiem     !!!!!!
# !!!!!   k papildinat ar dinamisku title   !!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#from django.core.context_processors import csrf # Form Komentari form security

import kamera.views.kamera_main as k # import page header/meta tags
from main.paginator import Paginator  # import paginator

from galerija.models import Galerija, GalerijaKoment, GalerijaLike

import math     # for rounding up Page Counter
import datetime


# GRID
def main(request, pageid=1):
    args = k.cam_header(request) # Header (Tabs, e.t.c. from app kamera)
    args['heading'] = u'Lietotāju attēlu galerija'

    if int(pageid) < 1:	# negative page number --> 404
        return redirect ('/')

    bildes = Galerija.objects.all()

    img_on_page = 20
    pagecount = int(math.ceil( int(bildes.count()) / float( img_on_page ))) # integer identical to range by count

    if int(pageid) > pagecount and int(pageid) > 1: # pageid exceeds pagecount --> 404
        return redirect ('/')

    start_img = int(pageid) * img_on_page - img_on_page	# start from image NR
    end_img = int(pageid) * img_on_page # end with image NR
    if end_img > bildes.count(): # if end NR exceeds limit set it to end NR
        end_img = bildes.count()

    args['images'] = bildes.order_by('-bilde_added')[start_img:end_img] # -argument is for negative sort
    args['paginator'] = Paginator( pagecount, pageid )

    args['galery_tab'] = True # For ACTIVE state "Lietotaju Galerija"

    response = render(request, 'gal_grid.html', args)
# SET page_location COOKIE
    response.set_cookie( key='page_location', value='/galery/' + str(pageid) +'/' )
    return response

# ===============================================================================================================================

def img_big(request, pageid, imgid):
    try:
        bilde = Galerija.objects.get( id = imgid ) # get image to display
    except ObjectDoesNotExist:	# not existing bilde --> 404
        return redirect ('galerija_main')
    if int(pageid) < 1: # negative page number --> 404
        return redirect ('galerija_main')

    bildes = Galerija.objects.all().order_by('-bilde_added')
    img_on_page = 20
    pagecount = int(math.ceil( int(bildes.count()) / float( img_on_page )))    # integer identical to range by .count()
    if int(pageid) > pagecount: # pageid exceeds pagecount --> 404
        return redirect ('galerija_main')

    args = k.cam_header(request) # Header (Tabs, e.t.c. from app kamera)

#    args.update(csrf(request))      # ADD CSRF TOKEN

    if request.POST and ("pause"+str(imgid) not in request.session): # IF COMMENT ADDED -->
        comment = request.POST.get('comment', '')
        if comment != '': # COMMENT NOT EMPTY -->
            new_comment = GalerijaKoment(koment_bilde = bilde, koment_text = comment) # create coment
            new_comment.save() # save comment

            request.session.set_expiry(60)
            request.session['pause'+str(imgid)] = True

            return redirect('galerija_img', pageid = pageid, imgid = imgid) # reload this view (prevents resend POST on refresh page)

    args['heading'] = u'Lietotāju attēlu galerija'
    args['image'] = bilde
    args['time'] = bilde.bilde_datums
    args['title'] = 'Lietotāju galerija | ' + k.get_domain_full(request) # title + DOMAIN

    args['komenti'] = GalerijaKoment.objects.filter( koment_bilde = bilde).order_by('-koment_datums')
    args['komenti_counter'] = args['komenti'].count()
    try:
        img_likes = GalerijaLike.objects.get( bilde = bilde )
        args['bilde_plus'] = img_likes.bilde_plus
        args['bilde_minus'] = img_likes.bilde_minus
    except:
        args['bilde_plus'] = 0
        args['bilde_minus'] = 0
#        pass

# Getting Next and Previous Bilde objects from filtered list
    counter = 0 # set iteration counter
    for img in bildes:
        if img == bilde:	# if image from this iteration == curent image do:
            try:	# try is for if previous does not exist
                args['back_img'] = bildes[counter - 1]  # get next object
            except:
                pass
            try:	# try is for if next does not exist
                args['next_img'] = bildes[counter + 1]  # get next object
            except:
                pass
            return_page = ( counter / 20 ) + 1	# locates page number you ar at the moment
        counter += 1	# increase iteration counter
    args['back_page'] = return_page

    response = render(request, 'gal_image.html', args)
# SET page_location COOKIE
#    response.set_cookie( key='page_location', value='/cam/img/'+ str(pageid) +'/'+ str(imgid) +'/' )
    return response


# =========================================================================================================
# LIKE
def img_plus(request, pageid, imgid):
    if request.POST and ("like"+str(imgid) not in request.session): # IF like already added
        bilde = Galerija.objects.get( id = imgid )
        try:
            temp = GalerijaLike.objects.get(bilde = bilde)
            temp.bilde_plus += 1
            temp.last_entry = datetime.datetime.now()
            temp.save()
        except:
            temp = GalerijaLike( bilde = bilde, bilde_plus = 1 )
            temp.save()

    request.session.set_expiry(60)
    request.session['like'+str(imgid)] = True

    return redirect('galerija_img', pageid = pageid, imgid = imgid) # reload this view (prevents resend POST on refresh page

# DISLIKE
def img_minus(request, pageid, imgid):
    if request.POST and ("like"+str(imgid) not in request.session): # IF like already added
        bilde = Galerija.objects.get( id = imgid )
        try:
            temp = GalerijaLike.objects.get(bilde = bilde)
            temp.bilde_minus += 1
            temp.last_entry = datetime.datetime.now()
            temp.save()
        except:
            temp = GalerijaLike( bilde = bilde, bilde_minus = 1 )
            temp.save()

    request.session.set_expiry(60)
    request.session['like'+str(imgid)] = True

    return redirect('galerija_img', pageid = pageid, imgid = imgid) # reload this view (prevents resend POST on refresh page)
