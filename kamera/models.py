# -*- coding: utf-8 -*-
from django.db import IntegrityError

from django.utils import timezone
from django.db import models
import uuid
import os
import random
import string

import datetime

KAMERA_TYPE = (
    ('PUB', 'public'),
    ('PRIV', 'private'),
    ('SEC', 'security'),
)

def image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    folder = datetime.datetime.now().strftime('%Y_%W')
    filename = "%s/%s.%s" % (folder, uuid.uuid4(), ext.lower()) # year_week/uuid.jpg
    return os.path.join('', filename)

def thumb_file_path(instance, filename):
    ext = filename.split('.')[-1]
    folder = datetime.datetime.now().strftime('%Y_%W')
    filename = "thumb/%s/%s.%s" % (folder, uuid.uuid4(), ext.lower()) # thumb/year_week/uuid.jpg
    return os.path.join('', filename)

def rand_slug():
    return str( uuid.uuid4() ).split("-")[4]


# !!!!! CLASS Kameras
class Kamera(models.Model):
    class Meta():
        db_table = "kameras"

    kamera_nos = models.CharField( max_length = 100 )
    kamera_slug = models.SlugField( unique = True, default=rand_slug() )
    kamera_apraksts = models.TextField( default = 'kameras apraksts', blank = True )
    kamera_img_dir = models.CharField( max_length = 50, default = 'username' )
    kamera_email = models.CharField( max_length = 30, blank = True )
    kamera_type = models.CharField( max_length=10, choices=KAMERA_TYPE, default="PUB" )

   # AI render
    kamera_ai = models.BooleanField( default = False )

    def __unicode__(self):
        return '%s' % (self.kamera_nos)


# !!!!! CLASS Bilde
class Bilde(models.Model):
    class Meta():
        db_table = "bildes"

    bilde_nos = models.CharField( max_length = 60 )
    bilde_bilde = models.ImageField( blank = True, null=True, upload_to = image_file_path )	# upload_to = image_image_path,
    bilde_thumb = models.ImageField( blank = True, null=True, upload_to = thumb_file_path )	# upload_to = thumb_image_path,
    bilde_datums = models.DateTimeField( default = timezone.now )
    bilde_kamera_id = models.ForeignKey( Kamera, default = 1 )

    def __unicode__(self):	# Return bilde_nos in ADMIN section instead of "Bilde object"
        return 'Bilde: ' + self.bilde_nos

    # object method rewriten for refresh funtion
    @classmethod
    def create(cls, bilde_nos, bilde_kamera_id, bilde_datums, bilde_bilde, bilde_thumb):
        img = cls( bilde_nos = bilde_nos, bilde_kamera_id = bilde_kamera_id , bilde_datums = bilde_datums, bilde_bilde = bilde_bilde, bilde_thumb = bilde_thumb )
        return img

