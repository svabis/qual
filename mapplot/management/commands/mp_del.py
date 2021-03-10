# -*- coding: utf-8 -*-
from __future__ import division
from datetime import datetime

from django.conf import settings

from django.core.management.base import BaseCommand, CommandError
from mapplot.models import MapPlotCity, MapPlot



# command
class Command(BaseCommand):
    help = "komanda"
    def handle(self, *args, **options):

        kusa = MapPlotCity.objects.get(name = "Kusa")
        print(kusa)

        points = MapPlot.objects.filter( city=kusa )

       # iterate last lines
        for p in points:
            print( p )
            p.deleted = True
            p.save()
