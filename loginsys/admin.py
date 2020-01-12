# -*- coding: utf-8 -*-
from django.contrib import admin
from loginsys.models import User_pin, User_data, User_kamera, Username_list


# User PIN MODEl
class User_pinAdmin(admin.ModelAdmin):
    fields = ['user_user', 'user_pin', ]
    list_display = ['user_user', 'user_pin', ]


# !!!!! User_data MODEL
class User_dataAdmin(admin.ModelAdmin):
    def visit_date(self, obj):
        return obj.user_last_visit.strftime("%Y/%b/%d  %H:%M")

    visit_date.short_description = 'Pēdējais apmeklējums'

    fields = ['user_user', 'user_last_visit', 'user_outside_mail', 'user_last_mail_check', 'user_mail_pasword']
    list_display = ['user_user', 'user_last_visit', 'user_outside_mail', 'user_last_mail_check', 'user_mail_pasword']


# !!!!! User_kamera MODEL
class User_kameraAdmin(admin.ModelAdmin):
    list_display = ['user', 'kamera']
    list_filter = ['user']

# !!!!! Username_list
class Username_listAdmin(admin.ModelAdmin):
    list_display = ['username', 'user_email', 'datums', 'kamera', 'kamera_type']


admin.site.register(User_pin, User_pinAdmin)
admin.site.register(User_data, User_dataAdmin)
admin.site.register(User_kamera, User_kameraAdmin)
admin.site.register(Username_list, Username_listAdmin)
