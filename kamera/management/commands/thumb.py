# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)
import datetime # for file create field
import pytz	# to set timezone
import cv2      # image container reader
from PIL import Image, ImageDraw

from django.utils.timezone import localtime

# IMPORT DJANGO STUFF
from django.core.files import File	# for file opening

from django.core.exceptions import MultipleObjectsReturned

from django.core.management.base import BaseCommand, CommandError
from kamera.models import Kamera, Bilde
from galerija.models import Galerija

class Command(BaseCommand):
  help = 'Refresh Bildes database'
  def handle(self, *args, **options):

        path = "/www/kuvalda/media/"
#    for cam in Kamera.objects.all():
#        bildes = Bilde.objects.filter(bilde_kamera_id = cam)
        bildes = Galerija.objects.all()

        for obj in bildes:
                            print obj
                            open_image = open(path + str(obj.bilde_bilde), 'rb')
                            image_file = File(open_image)

                            infile = path + str(obj.bilde_bilde)
                            outfile = '/www/kuvalda/misc/temp.jpg'
                            size = 200, 200         # THUMBNAIL MAXIMUM SIZE

                            try:
        # STANDART WAY TO CREATE THUMBNAIL FROM FILE
                                im = Image.open(infile)         # OPEN IMAGE FULL SIZE
                                im.thumbnail(size)              # RESIZE
                            except IOError:
        # NEW WAY TO CREATE THUMB FROM BROKEN IMAGES
                                print 'THUMB ERR 1'
                                try:
                                    tempfile = cv2.imread( infile )
                                    cv2.imwrite(outfile, tempfile ) # WRITE TEMPORARY FULL SIZE
                                    im = Image.open( outfile )      # OPEN TEMPORARY FULL SIZE
                                    im.thumbnail( size )            # RESIZE
                                except:
                                    print 'THUMB ERR 2'
                                    pass

        # SAVE TEMPORARY thumbnail FILE FOR UPLOAD TO /media/thumb/
                            im.save( '/www/kuvalda/misc/thumb.jpg', "JPEG")
                            thumb = open('/www/kuvalda/misc/thumb.jpg', 'rb')
                            thumb_file = File(thumb)   # create thumbnail

        # CREATE NEW Bilde OBJECT
                            obj.bilde_thumb = thumb_file
                            obj.save()      # save new object Bilde into database

                           # SET OWNER AND GROUP FOR IMAGE FILES IN /media/ FOLDER
                            os.system('sudo chown www-data:varwwwusers /www/kuvalda/media/' + str(obj.bilde_bilde))
                            os.system('sudo chown www-data:varwwwusers /www/kuvalda/media/' + str(obj.bilde_thumb))
