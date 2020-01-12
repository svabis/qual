# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models
import uuid
import os

def image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext.lower())
    return os.path.join('galery/', filename)

def thumb_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext.lower())
    return os.path.join('galery/thumb/', filename)


# !!!!! CLASS Bilde !!!!!
class Galerija(models.Model):
    class Meta():
        db_table = "galerija"

    bilde_nos = models.CharField( max_length = 60 )
    bilde_bilde = models.ImageField( blank = True, null=True, upload_to = image_file_path ) # upload_to = image_image_path,
    bilde_thumb = models.ImageField( blank = True, null=True, upload_to = thumb_file_path ) # upload_to = thumb_image_path,
    bilde_datums = models.DateTimeField( default = timezone.now )
    bilde_added = models.DateTimeField( default = timezone.now )
#    bilde_user = models.CharField( max_length = 30 )

    bilde_like = models.IntegerField( default = 0 )
#    bilde_kamera_id = models.ForeignKey( Kamera, default = 1 )

    def __unicode__(self):	# Return bilde_nos in ADMIN section instead of "Bilde object"
        return 'Bilde: ' + self.bilde_nos



# !!!!! CLASS GalerijaKoment !!!!!
class GalerijaKoment(models.Model):
    class Meta():
        db_table = "galerija_koment"

    koment_bilde = models.ForeignKey( Galerija, default = 1 )
    koment_datums = models.DateTimeField( default = timezone.now )
    koment_text = models.CharField( max_length = 150 )

#    koment_ip = models.CharField( max_length = 20, blank = True )
#    koment_user = 

#    def __unicode__(self):
#        return 'Komentars:  ' + self.koment_bilde # ERROR str+object


# Galerijas Bilžu +/-
class GalerijaLike(models.Model):
    class Meta():
        db_table = "galerija_like"

    last_entry = models.DateTimeField( default = timezone.now )
    bilde = models.ForeignKey( Galerija, blank=True, null=True )

    bilde_plus = models.IntegerField( default = 0 )
    bilde_minus = models.IntegerField( default = 0 )
