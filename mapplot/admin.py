# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import MapPlotCity, MapPlotUserCity
from .models import MapPlotType
from .models import MapPlot, MapPlotImage


# CITY
class MapPlotCityAdmin(admin.ModelAdmin):
    fields = ['name', 'lat', 'lon', 'zoom']
    list_display = ['name', 'lat', 'lon', 'zoom']

# USER <-> CITY
class MapPlotUserCityAdmin(admin.ModelAdmin):
    fields = ['user', 'city']
    list_display = ['user', 'city']

# POIN TYPE
class MapPlotTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'color', 'size']
    list_display = ['name', 'color', 'size']


# POINTS
class MapPlotAdmin(admin.ModelAdmin):
    fields = ['create_date', 'edit_date',
              'user',
              'deleted', 'mark', 'city',
              'lat', 'lon',
              'cur_lat', 'cur_lon', 'device',
              'radio',
              'chk_1', 'chk_2', 'chk_3']
    list_filter = ['create_date', 'edit_date', 'city_id', 'deleted', 
              'user',
              'radio',
              'chk_1', 'chk_2', 'chk_3']
    list_display = ['create_date', 'edit_date',
              'user',
              'deleted', 'mark', 'city',
              'lat', 'lon',
              'cur_lat', 'cur_lon', 'device',
              'radio',
              'chk_1', 'chk_2', 'chk_3']


# IMAGES FOR POINTS
class MapPlotImageAdmin(admin.ModelAdmin):
    fields = ['date', 'point', 'image']
    list_filter = ['date']
    list_display = ['date', 'point']


admin.site.register(MapPlotCity, MapPlotCityAdmin)
admin.site.register(MapPlotUserCity, MapPlotUserCityAdmin)

admin.site.register(MapPlotType, MapPlotTypeAdmin)

admin.site.register(MapPlot, MapPlotAdmin)
admin.site.register(MapPlotImage, MapPlotImageAdmin)

