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

import calendar

# !!!!! DST !!!!!
def dst(temp_date):
    today = temp_date.date()
    year = today.year

    dst_start = max(week[-1] for week in calendar.monthcalendar(year, 10)) # last sunday of this years Oct
    dst_end   = max(week[-1] for week in calendar.monthcalendar(year, 3))  # last sunday of this years Mar
   # convert to date objects
    date_dst_start = datetime.date(year, 10, dst_start)
    date_dst_end = datetime.date(year, 3, dst_end)
   # compare if in range (summer --> True)
    if date_dst_end <= today <= date_dst_start:
        return 1
    else:
        return 0


class Command(BaseCommand):
  help = 'Refresh Bildes database'
  def handle(self, *args, **options):
#    path_array = []
    for cam in Kamera.objects.all():
        path = "/home/" + cam.kamera_img_dir + "/"	# path to images
        imagelist = []  # array of pictures

       # If Camera AI enabled
        if cam.kamera_ai == True and len(os.listdir(path)) > 0:
            os.system("/home/svabis/web/utils/ai/runner.sh") # > /dev/null 2>&1 || true")

        try:
     # Fill picture Directory list array
          for filename in os.listdir(path):
             if filename.endswith(".JPG") or filename.endswith(".jpg"):

                 stat = os.stat(path + filename) # stat <-- file parameter object
                 c_date = datetime.datetime.fromtimestamp( stat.st_ctime ) # file creation time
                 tz = pytz.timezone('EET')       # Timezone info (image creation time does not include)
                 create_date = c_date.replace(tzinfo=tz) # - datetime.timedelta( hours = dst( c_date.replace(tzinfo=tz) ))    # repalcing timezone info


        # IF FILE IS BEING CREATED
                 timeDiff = ( datetime.datetime.now() - c_date ).total_seconds()
                 if timeDiff > 1:
                     try:
                            obj = Bilde.objects.get(bilde_nos = filename, bilde_kamera_id = cam)   # object exist do nothing
#                            print 'object exist:'
#                            print path + filename

                     except MultipleObjectsReturned:
                            print 'MultipleObjectsReturned:'
                            print path + filename

      	             except Bilde.DoesNotExist:      # start sequence what to do if file is not in database
                            open_image = open(path + filename, 'rb')
                            image_file = File(open_image)

                            infile = path + filename
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
        # GET FILE CREATION TIME AND CONVERT INTO TEXT
#                            time = stat
#                            text_1 = str(datetime.datetime.fromtimestamp( time.st_ctime ).strftime('%d/%m/%Y'))
#                            text_2 = str(datetime.datetime.fromtimestamp( time.st_ctime ).strftime('%H:%M'))

         # SET COLOR ODD/PAIR DAYS DIFFERENT
#                            col_date = int(datetime.datetime.fromtimestamp( time.st_ctime ).strftime('%d'))
#                            if col_date % 2 == 0:
#                                col_fill = (255, 255, 179)
#                            else:
#                                col_fill = (204, 255, 153)
#                            col_line = (0, 0, 0)

        # DRAW RECTANGLE AND TEXT ON thumbnail
#                            draw = ImageDraw.Draw(im)
#                            draw.rectangle([(130, 0), (199, 25)], fill = col_fill, outline = col_line )
#                            draw.text((135, 2), text_1, fill = col_line, font = None, anchor = None)
#                            draw.text((165, 13), text_2, fill = col_line, font = None, anchor = None)
#                            del draw

        # SAVE TEMPORARY thumbnail FILE FOR UPLOAD TO /media/thumb/
                            im.save( '/www/kuvalda/misc/thumb.jpg', "JPEG")
                            thumb = open('/www/kuvalda/misc/thumb.jpg', 'rb')
                            thumb_file = File(thumb)   # create thumbnail

        # CREATE NEW Bilde OBJECT
                            obj = Bilde.create( filename, cam, create_date, image_file, thumb_file)
                            obj.save()      # save new object Bilde into database
#                            print obj.bilde_bilde
#                            print obj.bilde_thumb

        # Remove / from .tar filename
#                            tar_name = str(cam.kamera_img_dir) # .tar filename

#                            if len(tar_name.split('/')) > 1:
#                                tar_name = tar_name.split('/')[0] + tar_name.split('/')[1] + '.tar'
#                            else:
#                                tar_name = tar_name + '.tar'

        # Check for Backup file (if needed create one) and append file to the backup file
#                            back_up_path = '/home/svabis/TrailCamPhoto/'
#                            if os.path.isfile(back_up_path + tar_name) == True: # BackUp File Exist
#                                comand = 'tar --update -f ' + back_up_path + tar_name + ' ' + infile.replace(" ", "\ ")
#                            else: # BackUp File does not exist (create) and append ile
#                                comand = 'tar -c -f ' + back_up_path + tar_name + ' ' + infile.replace(" ", "\ ")

                           # Append Source File to .tar
#                            os.system(comand + ' &> /dev/null') # disable output from bash command

                           # SET OWNER AND GROUP FOR IMAGE FILES IN /media/ FOLDER
                            os.system('sudo chown www-data:varwwwusers /www/kuvalda/media/' + str(obj.bilde_bilde))
                            os.system('sudo chown www-data:varwwwusers /www/kuvalda/media/' + str(obj.bilde_thumb))

        # DELETE IMAGE FILE FROM SYSTEM FOLDER
                            os.remove( path+filename )

        except Exception, e:
           print 'BIG ERR'
           print e
           print path
           print
           pass
