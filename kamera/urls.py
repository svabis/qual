from django.conf.urls import patterns, include, url

urlpatterns = [
# GRID
    url(r'^grid/(?P<camid>\w+)/(?P<pageid>\-\d+|\d+|\+\d+)/$', 'kamera.views.cam_id_grid', name='cam_id_grid'),

# DELETE GRID (POST)
    url(r'^grid_del/(?P<camid>\w+)/(?P<pageid>\-\d+|\d+|\+\d+)/$', 'kamera.views.grid_del', name='grid_del'),


# IMAGE

# FULLSIZE IMAGE /YYYY_WW/uuid4.jpg
    url(r'^img/(?P<pageid>\d+)/(?P<date>[0-9]{4}\_[0-9]{2})/(?P<imgid>[-\w]+)/$', 'kamera.views.bilde_id', name='bilde_id'),
    url(r'^img/(?P<pageid>\d+)/(?P<date>[0-9]{4}\_[0-9]{2})/(?P<imgid>[-\w]+)/(?P<show>\w+)/$', 'kamera.views.bilde_id', name='bilde_id'),
# FULLSIZE IMAGE unsorted
    url(r'^img/(?P<pageid>\d+)/(?P<imgid>[-\w]+)/$', 'kamera.views.bilde_id', name='bilde_id'),
    url(r'^img/(?P<pageid>\d+)/(?P<imgid>[-\w]+)/(?P<show>\w+)/$', 'kamera.views.bilde_id', name='bilde_id'),

# DELETE IMAGE
    url(r'^img/del/(?P<pageid>\d+)/(?P<date>[0-9]{4}\_[0-9]{2})/(?P<del_id>[-\w]+)/$', 'kamera.views.bilde_del', name='bilde_del'),
    url(r'^img/del/(?P<pageid>\d+)/(?P<del_id>[-\w]+)/$', 'kamera.views.bilde_del', name='bilde_del'),

# LIKE
#    url(r'^bilde/patik/(?P<pageid>\d+)/(?P<likeid>\w+\-\w+\-\w+\-\w+\-\w+)/$', 'kamera.views.bilde_like', name='bilde_like'),

# SHARE
    url(r'^img/share/(?P<pageid>\d+)/(?P<date>[0-9]{4}\_[0-9]{2})/(?P<shareid>[-\w]+)/$', 'kamera.views.share', name='bilde_share'),
    url(r'^img/share/(?P<pageid>\d+)/(?P<shareid>[-\w]+)/$', 'kamera.views.share', name='bilde_share'),


# ===== MAIN KAMERA VIEWS =====

# SORT ORDER --> MAIN
    url(r'^(?P<sort>\d+)/$', 'kamera.views.cam_sort_type'),

# MAIN (DEFAULT SORT)
    url(r'^$', 'kamera.views.cam_all', name='kameras_main'),
]

