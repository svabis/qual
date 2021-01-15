# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from django.utils import timezone

from mapplot.models import MapPlot, MapPlotCity
from mapplot.forms import MapPlotForm

from kamera.views import kamera_main


# ==================================================================================================================================================
# !!!!! MAPPLOT MAIN & ADD NEW !!!!!
def plot(request):
    args = kamera_main.cam_header(request)

   # LIMIT ACCES TO GROUP MEMBERS
    if not args['username'].groups.filter(name__in=["map_admin", "map_doer"]).exists():
#    if not args['username'].groups.filter(name="map_admin").exists():
        return redirect("/")

    args['title'] = 'Kartes plotteris | Svabwilla'
    args['heading'] = 'Kartes ploteris'

# !!!!!!!!!!!!!!!!!!!!
# !!!!! SET CITY !!!!!
# !!!!!!!!!!!!!!!!!!!!

#    args['city'] = MapPlotCity.objects.get( name="Madona" )
#    args['city'] = MapPlotCity.objects.get( name="TEST - Rīga" )
    args['city'] = MapPlotCity.objects.get( name="Ropaži" )

    args['data'] = MapPlot.objects.filter( deleted=False, city=args['city'] )

    args['form'] = MapPlotForm(initial={'city':args['city']})

    if request.POST:
        form = MapPlotForm( request.POST )
        c = request.POST['zoom']

        if form.is_valid():
            new_point = form.save( commit=False )

            try:
                temp = MapPlot.objects.filter(deleted=False, city=new_point.city, mark=new_point.mark)
                if temp.count() != 0:
                    args['form'] = form
                    args['error'] = "ID EXIST"
                    response = render(request, 'plot.html', args)
                    response.set_cookie( key='view', value=c, path='/') #, max_age=5 )
                    response.set_cookie( key='page_location', value='/plot/', path='/' )
                    return response
            except:
                pass

           # POINT VALIDATED
            form.save()
           # Set return to added Point
            response = redirect( '/mapplot/plot/')
            response.set_cookie( key='view', value=c, path='/') #, max_age=5 )
            return response

        else:
#            args['test'] = "viss slikti"
            args['form'] = form
            response = render(request, 'plot.html', args)
            response.set_cookie( key='view', value=c, path='/') #, max_age=5 )
            response.set_cookie( key='page_location', value='/plot/', path='/' )
            return response


    response = render(request, 'plot.html', args)
    response.set_cookie( key='page_location', value='/plot/', path='/' )
    return response



# ==================================================================================================================================================
# !!!!! MAPPLOT EDIT POINT !!!!!
def plot_edit(request, e_id):
    args = kamera_main.cam_header(request)

   # LIMIT ACCES TO GROUP MEMBERS
    if not args['username'].groups.filter(name__in=["map_admin", "map_doer"]).exists():
#    if not args['username'].groups.filter(name="map_admin").exists():
        return redirect("/")

    args['title'] = 'Kartes plotteris | Svabwilla'
    args['heading'] = 'Kartes ploteris'

# !!!!!!!!!!!!!!!!!!!!
# !!!!! SET CITY !!!!!
# !!!!!!!!!!!!!!!!!!!!

#    args['city'] = MapPlotCity.objects.get( name="Madona" )
#    args['city'] = MapPlotCity.objects.get( name="TEST - Rīga" )
    args['city'] = MapPlotCity.objects.get( name="Ropaži" )

    args['data'] = MapPlot.objects.filter(id=e_id)

    edit = MapPlot.objects.get( id=e_id )
    args['edit'] = edit

    args['form'] = MapPlotForm( instance=edit )

    if request.POST:
        form = MapPlotForm( request.POST, instance=edit )
        c = request.POST['zoom']

        if form.is_valid():
            edit_point = form.save( commit=False )

            try:
                temp = MapPlot.objects.filter(deleted=False, city=new_point.city, mark=new_point.mark)
                c = temp.count()
                if new_point in temp:
                    c = c - 1

                if c != 0:
                    args['form'] = form
                    args['error'] = "ID EXIST"
                    response = render(request, 'plot.html', args)
                    response.set_cookie( key='view', value=c, path='/') #, max_age=5 )
                    response.set_cookie( key='page_location', value='/plot/', path='/' )
                    return response
            except:
                pass

           # POINT VALIDATED
            edit_point.edit_date = timezone.now()
            form.save()
           # Set return to added Point
            response = redirect( '/mapplot/plot/')
            response.set_cookie( key='view', value=c, path='/') #, max_age=5 )
            return response

        else:
            args['test'] = "viss slikti"
            args['form'] = form
            response = render(request, 'plot.html', args)
            response.set_cookie( key='view', value=c, path='/') #, max_age=5 )
            response.set_cookie( key='page_location', value='/plot/', path='/' )
            return response


    response = render(request, 'plot.html', args)
    response.set_cookie( key='page_location', value='/plot/', path='/' )
    return response
