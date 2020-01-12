from django.db import models

# Create your models here.

# !!!!! Ip_list MODEL
class Ip_list(models.Model):
    class Meta():
        verbose_name = 'IP adreses'
        db_table = "ip_list"


    ip_ip = models.CharField( max_length = 20 ) # IP adress
    ip_remark = models.CharField( max_length = 200, blank=True )        # remark
    ip_time = models.DateTimeField( null=True, blank=True )     # last visit
    ip_count = models.IntegerField( default = 0 )       # visit counter

    def __unicode__(self):
        return u'%s' % (self.ip_ip)


# !!!!! Ip_hit MODEL
class Ip_hit(models.Model):
    class Meta():
        db_table = "ip_hit"

    ip_ip = models.CharField( max_length = 20 ) # IP adress
    ip_time = models.DateTimeField( null=True, blank=True )     # hit time
    ip_hit = models.CharField( max_length = 100 )       # hit location

    def __unicode__(self):
        return u'%s' % (self.ip_ip)


# !!!!! Ip_from MODEL
class Ip_from(models.Model):
    class Meta():
        verbose_name = 'IP no kurienes'
        db_table = "ip_from"

    ip_ip = models.CharField( max_length = 20 ) # IP adress
    ip_time = models.DateTimeField( null=True, blank=True )     # hit time
    ip_from = models.CharField( max_length = 150 )       # hit location

    def __unicode__(self):
        return u'%s' % (self.ip_ip)

