# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

#from django.utils import timezone

from mapplot.models import MapPlotCity
from mapplot.forms import MapPlotCityForm

from kamera.views import kamera_main


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
