# -*- coding: utf-8 -*-
from datetime import datetime
from datetime import timedelta
import pytz

from django.core.management.base import BaseCommand, CommandError

from kamera.models import Bilde
from animal.models import AnimalCoords

# command
class Command(BaseCommand):
  def handle(self, *args, **options):

    utc=pytz.UTC

    old = datetime.now() - timedelta(days=5*30)
    old_local = utc.localize( datetime.now() - timedelta(days=5*30) )

    for b in Bilde.objects.all():
     # check if Bilde is in AnimalCoords
      temp = AnimalCoords.objects.filter( a_img=b )
      if temp.count() != 0:
#        print b
#        print temp.count()
        print "IMAGE DETECTED"
        continue

      try:
        if b.bilde_datums < old:
          b.delete()
#          print ""
      except:
        try:
          if b.bilde_datums < old_local:
            b.delete()
#            print ""
        except:
          pass
#          print b.bilde_datums

    print
    print "all:\t" + str( Bilde.objects.all().count() )
