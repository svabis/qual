# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.models import User	# autorisation library
from django.contrib import auth			# autorisation library

from animal.models import AnimalType, AnimalCoords
from kamera.models import Bilde

from random import randint


def animal_counter(request):
    types = AnimalType.objects.all()
    for t in types:
      count = AnimalCoords.objects.filter(a_type=t).count()
      t.a_count = count
      t.save()


def get_domain(request):
    dot = str( request.META['HTTP_HOST'].split('.')[-1] )
    if dot == 'lv':
       # OUTPUT ==> Kuvlada.lv
        domain = 'Kuvalda.lv'
    else:
       # OUTPUT ==> TrailCamPhoto.<xx>
        domain = 'TrailCamPhoto.' + dot
    return domain

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# Main animal detector view
def animal_main(request):
    username = auth.get_user(request)
    if username.is_superuser == True or username.groups.filter(name='animal').exists():
        args = {}
        args['title'] = get_domain(request)
        args['username'] = auth.get_user(request)
        args['ip'] = get_client_ip(request)
        args['heading'] = "Animal Selector"

        args['animals'] = AnimalType.objects.all().order_by("a_type")

        images = Bilde.objects.all()
        nr = randint(0, images.count())
        args['img_nr'] = nr

        img = images[nr]
        args['img'] = img

        args['coords'] = AnimalCoords.objects.filter( a_img = img )

        response = render( request, 'animal_main.html', args )
        response.set_cookie( key='page_loc', value='/animal/', path='/' )
        return response

    return redirect('/auth/login/')

def animal_select(request, img_nr):
    img = Bilde.objects.all()[ int(img_nr) ]
    if request.POST:
       # get data from form
        x1 = int(request.POST.get('x1', ''))
        y1 = int(request.POST.get('y1', ''))
        x2 = int(request.POST.get('x2', ''))
        y2 = int(request.POST.get('y2', ''))
        select = int(request.POST.get('select', ''))
        another = request.POST.get('another', '')
       # if selected "other animal"
        if another != "":
            animal = AnimalType(a_type = another)
            animal.save()
        else:
            animal = AnimalType.objects.get(id=select)
        new_coords = AnimalCoords(a_type=animal, a_img=img, x1=x1, y1=y1, x2=x2, y2=y2)
        new_coords.save()
        animal_counter(request)

    return redirect('/animal/')



#      !!!!!!!!!!!!!!!!!!!!!!!!!!!
#      !!!!! selected images !!!!!
#      !!!!!!!!!!!!!!!!!!!!!!!!!!!
def animal_coords(request, img_nr):
    username = auth.get_user(request)
    if username.is_superuser == True or username.groups.filter(name='animal').exists():
        args = {}
        args['title'] = get_domain(request)
        args['username'] = auth.get_user(request)
        args['ip'] = get_client_ip(request)
        args['heading'] = "Animal Selector"

        args['animals'] = AnimalType.objects.all()
        args['img_nr'] = int(img_nr)

        img = AnimalCoords.objects.all()[ int(img_nr) ]
        args['img'] = img


        response = render( request, 'animal_coords.html', args )
        response.set_cookie( key='page_loc', value='/animal/coords'+str(img_nr), path='/' )
        return response

    return redirect('/auth/login/')
