from django.contrib import admin
from statistic.models import Ip_list, Ip_hit, Ip_from

class Ip_listAdmin(admin.ModelAdmin):
    list_display = ['ip_ip', 'ip_remark', 'ip_count', 'ip_time']
    list_filter = ['ip_ip', 'ip_time', 'ip_remark']


class Ip_hitAdmin(admin.ModelAdmin):
    list_display = ['ip_ip', 'ip_time', 'ip_hit']
    list_filter = ['ip_ip', 'ip_time']


class Ip_fromAdmin(admin.ModelAdmin):
    list_display = ['ip_ip', 'ip_time', 'ip_from']
    list_filter = ['ip_time']


admin.site.register(Ip_list, Ip_listAdmin)
admin.site.register(Ip_from, Ip_fromAdmin)
admin.site.register(Ip_hit, Ip_hitAdmin)

