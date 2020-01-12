from django.contrib import admin
from galerija.models import *

class GalerijaAdmin(admin.ModelAdmin):
    list_display = ['bilde_nos', 'bilde_bilde', 'bilde_thumb', 'bilde_datums', 'bilde_added',]
    fields = ['bilde_nos', 'bilde_bilde', 'bilde_thumb', 'bilde_datums', 'bilde_added',]
#    list_filter = []

class GalerijaKomentAdmin(admin.ModelAdmin):
    list_display = ['koment_datums', 'koment_bilde', 'koment_text']
    fields = ['koment_datums', 'koment_bilde', 'koment_text']
    list_filter = ['koment_datums', 'koment_bilde']

class GalerijaLikeAdmin(admin.ModelAdmin):
    list_display = ['last_entry', 'bilde_plus', 'bilde_minus', 'bilde']
    fields = ['bilde', 'last_entry', 'bilde_plus', 'bilde_minus']
    list_filter = ['last_entry']


admin.site.register(Galerija, GalerijaAdmin)
admin.site.register(GalerijaKoment, GalerijaKomentAdmin)
admin.site.register(GalerijaLike, GalerijaLikeAdmin)
