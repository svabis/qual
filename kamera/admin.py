# -*- coding: utf-8 -*-
from django.contrib import admin
from kamera.models import Kamera, Bilde
import datetime
import pytz


class KameraAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'kamera_slug': ('kamera_nos',),}
    list_display = ['kamera_nos', 'kamera_email', 'kamera_img_dir', 'kamera_type', 'kamera_ai', 'kamera_slug']
    fields = ['kamera_nos', 'kamera_apraksts', 'kamera_email', 'kamera_img_dir', 'kamera_type', 'kamera_ai']
    list_filter = ['kamera_email', 'kamera_type', 'kamera_ai']

class BildeAdmin(admin.ModelAdmin):
#    def bilde_date(self, obj):
# NEED TO REPLACE TIMEZONE
#        return obj.bilde_datums.strftime("%Y/%b/%d  %H:%M:%S") #.replace(tzinfo=pytz.timezone('EET'))

#    def bilde_name(self, obj):
#        return obj.bilde_nos

#    bilde_date.short_description = 'Bilde saņemta'
#    bilde_name.short_description = 'Attēla nosaukums'

    list_filter = ['bilde_datums', 'bilde_kamera_id']
    list_display = ['bilde_nos', 'bilde_datums', 'bilde_kamera_id']


admin.site.register(Kamera, KameraAdmin)
admin.site.register(Bilde, BildeAdmin)
