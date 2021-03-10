# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from mapplot.models import MapPlotCity
from mapplot.models import MapPlot

from kamera.views import kamera_main

import unicodedata

# export
from django.http import HttpResponse
# CSV
import csv
# XLS
import xlwt

from datetime import datetime

# ==================================================================================================================================================
# !!!!! MAPPLOT ECXELL EXPORT !!!!!
def city_export_xls(request, c_id):
    args = kamera_main.cam_header(request)

   # LIMIT ACCES TO GROUP ADMIN
    if not args['username'].groups.filter(name="map_admin").exists():
        return redirect("/")

   # GET CITY
    city = MapPlotCity.objects.get( id = c_id )
   # GET POINTS SORTED FOR CITY
    points = MapPlot.objects.filter( city = city, deleted = False ).order_by('mark')

    filename = unicodedata.normalize('NFKD', city.name).encode('ascii','ignore')
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="' + filename.lower() + '.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet( city.name )

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['DATE_ADD', 'DATE_EDIT', 'ID', 'LATITUDE', 'LONGITUDE', 'TYPE', 'OLD', 'LED', 'CONSOLE']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

   # HISTORY
    rows = points #.values_list('create_date', 'edit_date', 'mark', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3')
    for row in rows:
        row_num += 1
        ws.write(row_num, 0, row.create_date.strftime("%Y-%m-%d %H:%M"), font_style)
        try:
            ws.write(row_num, 1, row.edit_date.strftime("%Y-%m-%d %H:%M"), font_style)
        except:
            pass
        ws.write(row_num, 2, row.mark, font_style)
        ws.write(row_num, 3, row.lat, font_style)
        ws.write(row_num, 4, row.lon, font_style)
        ws.write(row_num, 5, row.radio.name, font_style)
        ws.write(row_num, 6, row.chk_1, font_style)
        ws.write(row_num, 7, row.chk_2, font_style)
        ws.write(row_num, 8, row.chk_3, font_style)


    wb.save(response)
    return response
