# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
import pytz

from django.core.management.base import BaseCommand, CommandError

from kamera.models import Kamera, Bilde
from animal.models import AnimalCoords

# command
class Command(BaseCommand):
  def handle(self, *args, **options):

    utc=pytz.UTC
   # regular delete
    old = datetime.now() - timedelta(days=40)
    old_local = utc.localize( datetime.now() - timedelta(days=50) )

   # truši delete
    t_old = datetime.now() - timedelta(days=10)
    t_old_local = utc.localize( datetime.now() - timedelta(days=15) )

    c_t_a = Kamera.objects.get(kamera_slug='LHpOrpMf')
    c_t_b = Kamera.objects.get(kamera_slug='nZsytvjs')

    for b in Bilde.objects.all():
     # check if Bilde is in AnimalCoords
      temp = AnimalCoords.objects.filter( a_img=b )
      if temp.count() != 0:
#        print "IMAGE DETECTED"
        continue

      if b.bilde_kamera_id == c_t_a or b.bilde_kamera_id == c_t_b:
         # truši delete
#          print b.bilde_kamera_id
          try:
            if b.bilde_datums < t_old:
              b.delete()
          except:
            try:
              if b.bilde_datums < t_old_local:
                b.delete()
            except:
              print(b.bilde_datums)
#              pass

     # regular delete
      try:
        if b.bilde_datums < old:
          b.delete()
      except:
        try:
          if b.bilde_datums < old_local:
            b.delete()
        except:
          print(b.bilde_datums)
#          pass

    print
    print "all:\t" + str( Bilde.objects.all().count() )
