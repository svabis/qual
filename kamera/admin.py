# -*- coding: utf-8 -*-
from django.contrib import admin
from kamera.models import Kamera, Bilde
import datetime
import pytz


class KameraAdmin(admin.ModelAdmin):
#    prepopulated_fields = {'kamera_slug': ('kamera_nos',),}
    list_display = ['kamera_nos', 'kamera_email', 'kamera_img_dir', 'kamera_type', 'kamera_ai', 'kamera_ftp', 'kamera_slug', 'kamera_apraksts_short']
    fields = ['kamera_nos', 'kamera_apraksts', 'kamera_email', 'kamera_img_dir', 'kamera_type', 'kamera_ai', 'kamera_ftp']
    list_filter = ['kamera_type', 'kamera_ai', 'kamera_ftp']

class BildeAdmin(admin.ModelAdmin):
    list_filter = ['bilde_datums', 'bilde_kamera_id']
    list_display = ['bilde_nos', 'bilde_datums', 'bilde_kamera_id']


admin.site.register(Kamera, KameraAdmin)
admin.site.register(Bilde, BildeAdmin)
