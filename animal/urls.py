# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = [
# SELECTED IMAGES
    url(r'^coords(?P<img_nr>\d+)$', 'animal.views.animal_coords'),

# SELECT & NEXT | SELECT & CONTINUE SELECT
    url(r'^select(?P<img_nr>\d+)$', 'animal.views.animal_select'),

# MAIN
    url(r'^$', 'animal.views.animal_main', name='animal_main'),
]
