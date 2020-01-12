# -*- coding: utf-8 -*-
import os       # for work with filesystem
#import cv2      # image container reader
from PIL import Image

import unicodedata

from django.core.management.base import BaseCommand, CommandError

from animal.models import AnimalType, AnimalCoords


#path on desktop
out_path = "/home/svabis/AI/animal/"

#path to user folder for FTP download
export_path = "/home/svabis/animals/"

# media path
media_path = "/www/kuvalda/media/"



def output(filename, data, folder):
  with open(export_path + folder + "annotations/image (" + filename + ").xml", "w") as f:
    f.write("<annotation>\n")
    f.write("	<folder>images</folder>\n")
    f.write("	<filename>image (" + filename + ").jpg</filename>\n")
    f.write("	<path>" + out_path + folder + "image (" + filename + ").jpg</path>\n")
    f.write("	<source>\n")
    f.write("		<database>Unknown</database>\n")
    f.write("	</source>\n")
    f.write("	<size>\n")
    f.write("		<width>" + str(data.a_img.bilde_bilde.width) + "</width>\n")
    f.write("		<height>" + str(data.a_img.bilde_bilde.height) + "</height>\n")
    f.write("		<depth>3</depth>\n")
    f.write("	</size>\n")
    f.write("	<segmented>0</segmented>\n")
    f.write("	<object>\n")
#    f.write("		<name>" + str(data.a_type.a_type) + "</name>\n")
    f.write("		<name>animal</name>\n")
    f.write("		<pose>Unspecified</pose>\n")
    f.write("		<truncated>0</truncated>\n")
    f.write("		<difficult>0</difficult>\n")
    f.write("		<bndbox>\n")
    f.write("			<xmin>" + str(data.x1) + "</xmin>\n")
    f.write("			<ymin>" + str(data.y1) + "</ymin>\n")
    f.write("			<xmax>" + str(data.x2) + "</xmax>\n")
    f.write("			<ymax>" + str(data.y2) + "</ymax>\n")
    f.write("		</bndbox>\n")
    f.write("	</object>\n")
    f.write("</annotation>\n")


class Command(BaseCommand):
    help = "Export marked objects to user home directory for FTP upload"
    def handle(self, *args, **options):

        objects = AnimalCoords.objects.all()
        count = objects.count()
        t = int((count/5)*4)

        c = 1
        for data in objects[0:t]:
          try:
           # Save image file to output
            img_file = media_path + str(data.a_img.bilde_bilde)
            tempfile = Image.open( img_file )
#            tempfile = cv2.imread( img_file )
#            cv2.imwrite( export_path + "train/images/image (" + str(c) + ").jpg", tempfile )
            tempfile.save( export_path + "train/images/image (" + str(c) + ").jpg", "JPEG" )

           # create annotation file
            output(str(c), data, "train/")
            c += 1
          except:
            pass

        for data in objects[t:]:
          try:
           # Save image file to output
            img_file = media_path + str(data.a_img.bilde_bilde)
            tempfile = Image.open( img_file )
            tempfile.save( export_path + "validation/images/image (" + str(c) + ").jpg", "JPEG" )

           # create annotation file
            output(str(c), data, "validation/")
            c += 1
          except:
            pass


        animals = AnimalType.objects.all()
        temp = []
        for a in animals:
            temp.append( unicodedata.normalize('NFKD', a.a_type).encode('ascii','ignore') )

        print temp
