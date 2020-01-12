# -*- coding: utf-8 -*-
from kamera.models import Kamera, Bilde # import aplication models
import math     # for rounding up Page Counter

class Paginator(object):
	visible = True		# PAGINATOR ON/OFF
	big	= True		# <<<< / >>>> ON/OFF
	pages	= []

	active_page = 1
	pagecount = 1

# ARRAY 9 ELEMENTS
#                                     x
#EX: 1,  2, ..., ..., ..., ...,  13, 14, 15
#                     x
#EX: 1,  2, ..., 5,   6,   7,   ..., 14, 15
#        x
#EX: 1,  2,   3, ..., ..., ..., ..., 14, 15

#EX: 1,  2,  3,  4,  5,  6,  7,  8,  9		 9 PAGES OR LESS
#EX: 1,  2,  3,  4,  5,  6, ..,  9, 10		10 PAGES
#EX: 1,  2, ..,  5,  6,  7, .., 10, 11		11 PAGES OR MORE


# CONSTRUCTOR
	def __init__(self, count, current):
		self.active_page = int(current)
		self.pagecount = count
		self.pages = []

		if count < 2:			# IF PAGE IS ONE => PAGINATOR HIDEN
			self.visible = False
		else:
			self.visible = True
# NO "GAP'S"
		if count < 10:
			self.big = False
			for nr in range(count):
				self.pages.append( nr + 1 )
# ONE OR TWO "GAP'S"
		else:
			if int(current) < 6:
	# "GAP" IN THE END
				for nr in range(6):
	                                self.pages.append( nr + 1 )
				self.pages.append( 0 )
				self.pages.append( count-1 )
				self.pages.append( count )

			elif int(current) > (count-5):
	# "GAP" IN THE BEGINING
                                self.pages.append( 1 )
                                self.pages.append( 2 )
                                self.pages.append( 0 )
                                for nr in range(count-6, count):
                                        self.pages.append( nr + 1 )
	# TWO "GAP'S"
			else:
                                self.pages.append( 1 )
                                self.pages.append( 2 )
                                self.pages.append( 0 )		# GAP
                                self.pages.append( int(current) - 1 )
                                self.pages.append( int(current) )
                                self.pages.append( int(current) + 1 )
                                self.pages.append( 0 )		# GAP
                                self.pages.append( count-1 )
                                self.pages.append( count )

# piemēram ja ir tikai viena tad lapu dalītāja nav vispār	# DONE !!!
# ja ir līdz 10 -> sānu pogas nav un visur ir cipari		# DONE !!!
# ja  10 ... 13 tad viens "robs"
# ja vairāk -> viens "robs" ja galā, divi "robi" ja pa vidu...
