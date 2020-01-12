# -*- coding: utf-8 -*-
from django.contrib import admin
from animal.models import AnimalType, AnimalCoords


class AnimalTypeAdmin(admin.ModelAdmin):

    list_display = ['a_type', 'a_count']
    fields = ['a_type', 'a_count']
#    list_filter = []


class AnimalCoordsAdmin(admin.ModelAdmin):

    list_display = ['a_type', 'a_img', 'x1', 'y1', 'x2', 'y2']
#    fields = ['a_type', 'a_img', 'x1', 'y1', 'x2', 'y2']
    fields = ['a_type', 'x1', 'y1', 'x2', 'y2']
    list_filter = ['a_type']


admin.site.register(AnimalType, AnimalTypeAdmin)
admin.site.register(AnimalCoords, AnimalCoordsAdmin)
