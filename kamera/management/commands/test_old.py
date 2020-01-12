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

    old = datetime.now() - timedelta(days=10*30)
    old_local = utc.localize( datetime.now() - timedelta(days=10*30) )

    er = []

    for b in Bilde.objects.all():
     # check if Bilde is in AnimalCoords
      temp = AnimalCoords.objects.filter( a_img=b )
      if temp.count() != 0:
#        print b
#        print temp.count()
        print "IMAGE DETECTED"
        continue

#      try:
#        if b.bilde_datums < old:
#          print(b)
#          b.delete()
#      except:
#        try:
#          if b.bilde_datums < old_local:
#            print(b)
#            b.delete()
#        except:
#          print b.bilde_datums

    print
    print "all:\t" + str( Bilde.objects.all().count() )

    print len(er)
    print er
