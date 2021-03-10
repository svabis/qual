# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from django.utils import timezone

from mapplot.models import MapPlot, MapPlotCity

from mapplot.models import MapPlotCity, MapPlotUserCity
#from mapplot.forms import MapPlotForm

from kamera.views import kamera_main

def city_select(request):
    args = kamera_main.cam_header(request)

   # LIMIT ACCES TO GROUP MEMBERS
    if not args['username'].groups.filter(name__in=["map_admin", "map_doer"]).exists():
#    if not args['username'].groups.filter(name="map_admin").exists():
        return redirect("/")

    args["data"] = MapPlotUserCity.objects.filter(user=args['username']).order_by('city__name')

   # SELECT CITY IF ONLY ONE IS SET
    if len(args["data"]) == 1:
        city = args["data"][0].city.id
        response = redirect( '/mapplot/plot/' )
        try:
            response.delete_cookie('view')
        except:
            pass
        response.set_cookie( key='city', value=city, path='/') #, max_age=5 )
        return response

   # SELECT CITY FROM LIST
    if request.POST:
        city = request.POST['city']
        response = redirect( '/mapplot/plot/' )
        try:
            response.delete_cookie('view')
        except:
            pass
        response.set_cookie( key='city', value=city, path='/') #, max_age=5 )
        return response

    response = render(request, 'city_select.html', args)
#    response.set_cookie( key='view', value=c, path='/') #, max_age=5 )
    return response


# ==================================================================================================================================================
def plot_search(request):
    args = kamera_main.cam_header(request)

   # LIMIT ACCES TO GROUP MEMBERS
    if not args['username'].groups.filter(name__in=["map_admin", "map_doer"]).exists():
#    if not args['username'].groups.filter(name="map_admin").exists():
        return redirect("/")

    try:
        s = request.POST['search']
        edit = MapPlot.objects.filter(mark=s)[0]
        response = redirect( '/mapplot/plot/'+str(edit.id)+'/')
        return response

    except:
        response = redirect( '/mapplot/plot/')
        return response


# ==================================================================================================================================================
# !!!!! MAPPLOT DELETE !!!!!
def plot_del(request, d_id):
    args = kamera_main.cam_header(request)

   # LIMIT ACCES TO GROUP MEMBERS
    if not args['username'].groups.filter(name__in=["map_admin", "map_doer"]).exists():
#    if not args['username'].groups.filter(name="map_admin").exists():
        return redirect("/")

    plot = MapPlot.objects.get( id=d_id )
    plot.edit_date = timezone.now()
    plot.user = args['username']
    plot.deleted = True
    plot.save()

   # Set return to added Point
    c = plot.lat + ":" + plot.lon + ":" + "18"
    response = redirect( '/mapplot/plot/')
    response.set_cookie( key='view', value=c, path='/', max_age=5 )
    return response
