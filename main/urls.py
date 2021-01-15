from django.views.static import serve
from django.conf import settings

# STANDART
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from django.contrib.auth.decorators import login_required # LOGIN

# REST API
from rest_framework import routers
from mobile import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
#router.register(r'user_cam', views.User_kameraViewSet)
#router.register(r'cam', views.KameraViewSet)
router.register(r'img', views.BildeViewSet)


admin.autodiscover()
admin.site.login = login_required(admin.site.login)

urlpatterns = [
# GOOGLE CLOUD MESAGING (GCM)
    url(r'', include('gcm.urls')),

# mobile
    url(r'^mobile/', include(router.urls)), # name 'router' is not defined
#    url(r'^mobile_api/', views.Response_1),
#    url(r'^mobile_img/', views.cam_img),

# admin
 # Django REST
#    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
 # Django
    url(r'^admin9876/', include(admin.site.urls)),

# STATIC & MEDIA FOLDERS
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT,}),

# CONTAINER_SEARCH
    url(r'^container_search/', 'main.views.container_search'),
# CONTAINER_SEARCH
    url(r'^container_pdf/', 'main.views.container_pdf'),
# CONTAINER_PIN
    url(r'^container_pin/', 'main.views.container_pin'),

# MAPPLOT
    url(r'^mapplot/', include('mapplot.urls')),

# ANIMAL DETECTION
    url(r'^animal/', include('animal.urls')),

# LOGIN
    url(r'^auth/', include('loginsys.urls')),
# KAMERAS/BILDES
    url(r'^cam/', include('kamera.urls')),
# USER GALERIJA
    url(r'^gallery/', include('galerija.urls')),

# 500 error
    url(r'500', 'main.views.errorpage'),

# MAIN --> KAMERAS
    url(r'^', 'main.views.home'),
]
