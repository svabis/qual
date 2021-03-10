# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from mapplot.models import MapPlotCity
from mapplot.models import MapPlot

from kamera.views import kamera_main

#import unicodedata

#from django.http import HttpResponse

#import io
#from django.http import FileResponse
#from reportlab.pdfgen import canvas

#import pdfkit

#from datetime import datetime

# ==================================================================================================================================================
# !!!!! MAPPLOT PDF EXPORT !!!!!
def city_export_pdf(request, c_id):
    args = kamera_main.cam_header(request)

   # LIMIT ACCES TO GROUP MEMBERS
#    if not args['username'].groups.filter(name__in=["map_admin", "map_doer"]).exists():
    if not args['username'].groups.filter(name="map_admin").exists():
        return redirect("/")

    args['title'] = 'Kartes plotteris'
    args['heading'] = 'Kartes ploteris'

   # SET CITY
    args['city'] = MapPlotCity.objects.get( id=c_id )

    args['data'] = MapPlot.objects.filter( deleted=False, city=args['city'] )

#    args['form'] = MapPlotForm(initial={'city':args['city']})

    response = render(request, 'pdf.html', args)
    response.set_cookie( key='page_location', value='/plot/', path='/' )
    return response

