# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

#from django.utils import timezone

from mapplot.models import MapPlotCity, MapPlotUserCity

from mapplot.forms import MapPlotCityForm

from kamera.views import kamera_main


# ==================================================================================================================================================
# !!!!! MAPPLOT ADMIN (lvl2) !!!!!
def mapplot_admin(request):
    args = kamera_main.cam_header(request)

   # LIMIT ACCES TO GROUP ADMIN
    if not args['username'].groups.filter(name="map_admin").exists():
        return redirect("/")

    args["heading"] = u'Mapplot Admin sadaļa'
    args["title"] = u'Mapplot Admin sadaļa'

   # CITY
    args["city_data"] = MapPlotCity.objects.all().order_by('name')

   # USER
    u_data = []
    data = MapPlotUserCity.objects.all().order_by('user', 'city')
    temp_data = []
    try:
        temp = data[0].user
    except:
        temp = ""

    for d in data:
        groups = d.user.groups.all().values_list('name', flat=True)
        adm = True if "map_admin" in groups else False

        if temp == d.user:
            temp_data.append( [d, adm] )
        else:
            u_data.append( temp_data )
            temp_data = [[d, adm]]
        temp = d.user
    if len(u_data) != 0:
        u_data.append( temp_data )

    args["user_data"] = u_data

# !!!!!!!!!!!!!!!!!!!!!!!!!
# !!! PUT STUFF IN HERE !!!
# !!!!!!!!!!!!!!!!!!!!!!!!!

    response = render(request, 'mapplot_admin.html', args)
    return response

# ==================================================================================================================================================
# !!!!! ADD NEW CITY !!!!!
def city_add(request):
    args = kamera_main.cam_header(request)

   # LIMIT ACCES TO GROUP ADMIN
    if not args['username'].groups.filter(name="map_admin").exists():
        return redirect("/")

    args['data'] = MapPlotCity.objects.all()
    form = MapPlotCityForm

    if request.POST:
       # ADD CITY
        form = MapPlotCityForm( request.POST )
        if form.is_valid():
#            new_city = form.save( commit=False )
            form.save()
            response = redirect('city_add')
            return response

    args['form'] = form

    response = render(request, 'city_add.html', args)
    return response


# ==================================================================================================================================================
# !!!!! EDIT CITY !!!!!
def city_edit(request, c_id):
    args = kamera_main.cam_header(request)

   # LIMIT ACCES TO GROUP ADMIN
    if not args['username'].groups.filter(name="map_admin").exists():
        return redirect("/")

    args['data'] = MapPlotCity.objects.all()

    try:
        args['edit'] = MapPlotCity.objects.get(id=c_id)
    except:
        return redirect('city_add')

    form = MapPlotCityForm( instance=args['edit'] )

    if request.POST:
       # ADD CITY
        form = MapPlotCityForm( request.POST, instance=args['edit'] )
        if form.is_valid():
#            new_city = form.save( commit=False )
            form.save()
            response = redirect('city_add')
            return response

    args['form'] = form

    response = render(request, 'city_add.html', args)
    return response
