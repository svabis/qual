# -*- coding: utf-8 -*-
import os       # for work with filesystem
#import cv2      # image container reader
from PIL import Image

import unicodedata

from django.core.management.base import BaseCommand, CommandError

from animal.models import AnimalType, AnimalCoords


class Command(BaseCommand):
  help = "set coords right"
  def handle(self, *args, **options):

    objects = AnimalCoords.objects.all()
    e = []

    for d in objects:
      error = False

      if d.x1 > d.x2:
        temp = d.x1
        d.x1 = d.x2
        d.x2 = temp
        d.save()
        error = True

      if d.y1 > d.y2:
        temp = d.y1
        d.y1 = d.y2
        d.y2 = temp
        d.save()
        error = True

      if error == True:
        e.append(d)

    print(len(e))
    print(e)
