# -*- coding: utf-8 -*-
from django.db import models

from django.contrib.auth.models import User
from kamera.models import Kamera

from django.utils import timezone

# PIN
class User_pin(models.Model):
    class Meta():
        db_table = "user_pin"

    user_user = models.OneToOneField( User )
    user_pin = models.CharField( max_length = 30, blank = False, null = False )

    def __unicode__(self):
        return u'%s' % (self.user_user)


# !!!!! User_data MODEL
class User_data(models.Model):
    class Meta():
        db_table = "user_data"

    user_user = models.OneToOneField( User, related_name='u' )
    user_last_visit = models.DateTimeField( default = timezone.now )	# FOR LAST LOG (NOT AUTORIZATION)
    user_outside_mail = models.BooleanField( default = False )
    user_last_mail_check = models.DateTimeField( default = timezone.now )
    user_mail_pasword = models.CharField( max_length = 30, blank = True, null=True )

    def __unicode__(self):
        return u'%s' % (self.user_user)


# !!!!! User_data MODEL
class User_kamera(models.Model):
    class Meta():
        db_table = "user_kameras"

    user = models.ForeignKey( User, related_name='k' )
    kamera = models.ForeignKey( Kamera, related_name='kam' )

#    def __unicode__(self):      # Return user in ADMIN section instead of "User kameras object"
#        return self.user

# !!!!! User_data MODEL
class Username_list(models.Model):
    class Meta():
        db_table = "username_list"

    username = models.CharField( max_length = 30, default = '' )
    user_email = models.CharField( max_length = 50, default = '' )
    datums = models.DateTimeField( default = timezone.now )
    kamera = models.CharField( max_length = 30, default = '' )
    kamera_type = models.CharField( max_length = 6, default = 'PUB' )
    passw = models.CharField( max_length = 30, default = '' )
