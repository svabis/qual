# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from datetime import datetime


# !!!!! MAP PLOT CITY !!!!!
class MapPlotCity(models.Model):
    class Meta():
        db_table = "map_plot_city"
        verbose_name_plural = "Pilsētas"

    name = models.CharField( max_length=100, default="" )

    lat = models.CharField( max_length=50, default="" )
    lon = models.CharField( max_length=50, default="" )

    zoom = models.IntegerField( default=14 )

    def __unicode__(self):
        return '%s' % (self.name)

#    def __str__(self):
#        return self.name


# !!!!! MAP PLOT USER CITY !!!!!
class MapPlotUserCity(models.Model):
    class Meta():
        db_table = "map_plot_user_city"
        verbose_name_plural = "Lietotāji <--> Pilsētas"

    user = models.ForeignKey( User, on_delete=models.CASCADE, default=1 )
    city = models.ForeignKey( MapPlotCity, on_delete=models.CASCADE, default=1 )


# ================================================================================================
# !!!!! MAP PLOT POINTS !!!!!
class MapPlotType(models.Model):
    class Meta():
        db_table = "map_plot_point_type"
        verbose_name_plural = "Punktu tipi"

    name = models.CharField( max_length=50, default="" )
    color = models.CharField( max_length=20, default="" )
    size = models.IntegerField( default=3 )

    def __unicode__(self):
        return '%s' % (self.name)


class MapPlot(models.Model):
#'date', 'mark', 'city', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3'
    class Meta():
        db_table = "map_plot_points"
        verbose_name_plural = "Punkti"

    create_date = models.DateTimeField( default = timezone.now )
    edit_date = models.DateTimeField( blank=True, null=True )

    user = models.ForeignKey( User, on_delete=models.CASCADE, default=1 )

    mark = models.CharField( max_length=12, default="", blank=False )

    city = models.ForeignKey( MapPlotCity, on_delete=models.CASCADE, default=1 )

    lat = models.CharField( max_length=50 )
    lon = models.CharField( max_length=50 )

   # silent coords
    cur_lat = models.CharField( max_length=50, blank=True, null=True )
    cur_lon = models.CharField( max_length=50, blank=True, null=True )
   # device
    device = models.CharField( max_length=200, blank=True, null=True )

    radio = models.ForeignKey( MapPlotType, on_delete=models.CASCADE, default=1 )

    chk_1 = models.BooleanField( default=False )
    chk_2 = models.BooleanField( default=False )
    chk_3 = models.BooleanField( default=False )

   # dzēsts
    deleted = models.BooleanField( default=False )

    def __unicode__(self):
        return '%s' % (self.mark)


# !!!!! MAP IMAGES !!!!!
class MapPlotImage(models.Model):
    class Meta():
        db_table = "map_plot_images"
        verbose_name_plural = "Punktu attēli"

    date = models.DateTimeField( default = timezone.now )

    point = models.ForeignKey( MapPlot, on_delete=models.CASCADE, default=1, related_name='image' )

    image = models.ImageField( upload_to = "mapplot/" )
