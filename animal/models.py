# -*- coding: utf-8 -*-
from django.db import models

from kamera.models import Bilde


# !!!!! CLASS Animal Type
class AnimalType(models.Model):
    class Meta():
        db_table = "animal_type"

    a_type = models.CharField( max_length = 100 )
    a_count = models.IntegerField( default = 0 )

    def __unicode__(self):
        return '%s' % (self.a_type)



# !!!!! CLASS rectange coords on image & animal
class AnimalCoords(models.Model):
    class Meta():
        db_table = "animal_coords"

    a_type = models.ForeignKey( AnimalType, blank=True, null=True )
    a_img = models.ForeignKey( Bilde, blank=True, null=True )

    x1 = models.IntegerField( default = 0 )
    y1 = models.IntegerField( default = 0 )
    x2 = models.IntegerField( default = 0 )
    y2 = models.IntegerField( default = 0 )

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!! ADD USER who added for validation purposes !!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def __unicode__(self):
        return '%s' % (self.a_type)



