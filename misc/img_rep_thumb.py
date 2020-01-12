#!/usr/bin/python
# sudo apt-get install python-opencv
import cv2
from PIL import Image, ImageDraw
import os
import datetime

def thumb_draw(infile,outfile):
	# GET FILE CREATION TIME AND CONVERT INTO TEXT
	stat = os.stat( infile ) # stat <-- file parameter object
	text_1 = str(datetime.datetime.fromtimestamp( stat.st_ctime ).strftime('%d/%m/%Y'))
	text_2 = str(datetime.datetime.fromtimestamp( stat.st_ctime ).strftime('%H:%M'))

	# SET COLOR
	col_fill = (255, 255, 179)
	col_line = (0, 0, 0)

	# PREPARE IMAGE FOR DRAWING
	im = Image.open( outfile )
	draw = ImageDraw.Draw(im)
	draw.rectangle([(130, 0), (199, 25)], fill = col_fill, outline = col_line )
	draw.text((135, 2), text_1, fill = col_line, font = None, anchor = None)
	draw.text((165, 13), text_2, fill = col_line, font = None, anchor = None)
	del draw

	# SAVE THUMBNAIL WITH TEXT IN CORNER
	im.save( outfile, "JPEG" )


def thumb(input_file):
	infile = path + input_file
	outfile = path + "thumb/" + input_file	# OUTPUT FILENAME
	size = 200, 200		# THUMBNAIL MAXIMUM SIZE

	try:
	# STANDART WAY TO CREATE THUMBNAIL FROM FILE
		print "1"
		im = Image.open(infile)		# OPEN IMAGE FULL SIZE
		im.thumbnail(size)		# RESIZE
		im.save(outfile, "JPEG")	# SAVE THUMBNAIL FROM NORMAL IMAGE FILE
		thumb_draw(infile, outfile)
	except IOError:
	# NEW WAY TO CREATE THUMB FROM BROKEN IMAGES
		try:
			print "2"
			tempfile = cv2.imread( infile )
			cv2.imwrite(outfile, tempfile )	# WRITE TEMPORARY FULL SIZE
			im = Image.open( outfile )	# OPEN TEMPORARY FULL SIZE
			im.thumbnail( size )		# RESIZE
			im.save( outfile, "JPEG" )	# SAVE THUMBNAIL FROM BROKEN IMAGE FILE
			thumb_draw(infile, outfile)
		except:
			print "3"
	print infile

#path = '/kuvalda/media/'
path = '/home/svabis/'
#file = '600_3102.JPG'
file = '400_1780.JPG'

imagelist = []  # array of pictures

# Fill picture Directory list array
#for filename in os.listdir(path):
#	imagelist.append(filename)

#for file in imagelist:

thumb(file)
