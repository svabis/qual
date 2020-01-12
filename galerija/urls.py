from django.conf.urls import patterns, include, url

urlpatterns = [

# LIKE/DISLIKE
    url(r'^(?P<pageid>\d+)/(?P<imgid>\d+)/plus$', 'galerija.views.img_plus'),
    url(r'^(?P<pageid>\d+)/(?P<imgid>\d+)/minus$', 'galerija.views.img_minus'),

# FULLSIZE IMAGE /img/<page>/uuid4.jpg
#    url(r'^(?P<pageid>\d+)/galery/(?P<imgid>[-\w]+)/$', 'galerija.views.img_big'),
    url(r'^(?P<pageid>\d+)/(?P<imgid>\d+)/$', 'galerija.views.img_big', name='galerija_img'),

# GALLERY GRID VIEW
    url(r'^(?P<pageid>\d+)/$', 'galerija.views.main', name='galerija_page'),

# MAIN GALLERY VIEW
    url(r'^$', 'galerija.views.main', name='galerija_main'),

]

