# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import MapPlot, MapPlotCity, MapPlotImage


class MapPlotCityAdmin(admin.ModelAdmin):
    fields = ['name', 'lat', 'lon', 'zoom']
#    list_filter = ['name']
    list_display = ['name', 'lat', 'lon', 'zoom']

class MapPlotAdmin(admin.ModelAdmin):
    fields = ['create_date', 'edit_date',
              'deleted', 'mark', 'city',
              'lat', 'lon',
              'cur_lat', 'cur_lon', 'device',
              'radio', 'chk_1', 'chk_2', 'chk_3']
    list_filter = ['create_date', 'edit_date', 'city_id', 'deleted', 'radio', 'chk_1', 'chk_2', 'chk_3']
    list_display = ['create_date', 'edit_date',
              'deleted', 'mark', 'city',
              'lat', 'lon',
              'cur_lat', 'cur_lon', 'device',
              'radio', 'chk_1', 'chk_2', 'chk_3']


class MapPlotImageAdmin(admin.ModelAdmin):
    fields = ['date', 'point', 'image']
    list_filter = ['date']
    list_display = ['date', 'point']


admin.site.register(MapPlotCity, MapPlotCityAdmin)
admin.site.register(MapPlot, MapPlotAdmin)
admin.site.register(MapPlotImage, MapPlotImageAdmin)

