# -*- coding: utf-8 -*-
import os       # for work with filesystem
import re       # for regular expresions (regex)

# for random string :)
import random
import string


# IMPORT DJANGO STUFF
from django.core.files import File	# for file opening

from django.core.exceptions import MultipleObjectsReturned

from django.core.management.base import BaseCommand, CommandError
from kamera.models import Kamera, Bilde



class Command(BaseCommand):
    help = 'Refresh 100_1000.JPG names'
    def handle(self, *args, **options):

        bildes = Bilde.objects.all()
#        gravani = Kamera.objects.get( kamera_img_dir = 'u26962460' )
#        bildes = Bilde.objects.filter( bilde_kamera_id = gravani.id )

        count =0

        for obj in bildes:
#            temp = re.search("(^\d{3}\_\d{4}\.JPG$)", str(obj.bilde_nos))
            temp = re.search("(^\d{3}\_\d{4}\.JPG)", str(obj.bilde_nos))
            try:
#              print temp.group(0)
#              print obj.bilde_nos[:8]
#              obj.bilde_nos = temp.group(0)
#              obj.save()

              if temp.group(0) == str(obj.bilde_nos):
                count += 1
                obj.bilde_nos = obj.bilde_nos[:8] + '_' + ''.join(random.choice(string.ascii_letters) for _ in range(3)) + '.jpg'
                obj.save()
#                print str(obj.bilde_nos)
#                print temp.group(0)
            except:
              pass

        print count
