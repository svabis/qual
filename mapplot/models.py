# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from datetime import datetime


# !!!!! MAP PLOT CITY !!!!!
class MapPlotCity(models.Model):
    class Meta():
        db_table = "map_plot_city"

    name = models.CharField( max_length=100, default="" )

    lat = models.CharField( max_length=50, default="" )
    lon = models.CharField( max_length=50, default="" )

    zoom = models.IntegerField( default=14 )

#    def __str__(self):
#        return self.name


# !!!!! MAP PLOT POINTS !!!!!
PLOT_TYPES = (
    ('green', 'stabs'),
    ('red', 'kaste'),
#    ('blue', 'zils'),
)

class MapPlot(models.Model):
#'date', 'mark', 'city', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3'
    class Meta():
        db_table = "map_plot_points"

    create_date = models.DateTimeField( default = timezone.now )
    edit_date = models.DateTimeField( blank=True, null=True )

    mark = models.CharField( max_length=8, default="", blank=False )

    city = models.ForeignKey( MapPlotCity, on_delete=models.CASCADE, default=1 )

    lat = models.CharField( max_length=50 )
    lon = models.CharField( max_length=50 )
   # silent coords
    cur_lat = models.CharField( max_length=50, default="" )
    cur_lon = models.CharField( max_length=50, default="" )
   # device
    device = models.CharField( max_length=200, default="" )

    radio = models.CharField( max_length=10, choices=PLOT_TYPES, default="green")

    chk_1 = models.BooleanField( default=False )
    chk_2 = models.BooleanField( default=False )
    chk_3 = models.BooleanField( default=False )

   # dzēsts
    deleted = models.BooleanField( default=False )


# !!!!! MAP IMAGES !!!!!
class MapPlotImage(models.Model):
    class Meta():
        db_table = "map_plot_images"

    date = models.DateTimeField( default = timezone.now )

    point = models.ForeignKey( MapPlot, on_delete=models.CASCADE, default=1 )

    imgage = models.ImageField( upload_to = "mapplot/" )
