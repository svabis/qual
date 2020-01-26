from django.conf.urls import patterns, include, url

urlpatterns = [
   # LOGIN / LOGOUT
    url(r'^login/$', 'loginsys.views.login',),
    url(r'^logout/$', 'loginsys.views.logout',),

    url(r'^pin/$', 'loginsys.views.pin',),

   # EXISTING USER LIST
    url(r'^user_list/$', 'loginsys.views.existing_users',),

   # LOCAL E_MAIL LIST
    url(r'^email_list/$', 'loginsys.views.list_emails',),

   # REGISTRATION
#    url(r'^register/$', 'loginsys.views.register',),
   # ADD / DEL USER
#    url(r'^user_add/(?P<id>\d+)/$', 'loginsys.views.user_add',),
#    url(r'^user_del/(?P<id>\d+)/$', 'loginsys.views.user_del',),

   # NEW REGISTRED USERS (WAITING TO ACCEPT)
#    url(r'^new_users/$', 'loginsys.views.new_users',),

]

