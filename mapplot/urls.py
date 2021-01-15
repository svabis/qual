# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from .views import city_add, city_edit

from .views import plot, plot_edit, plot_del, plot_search


urlpatterns = [
# ADMIN
# ============================================================
# CITY ADD
   url(r'city_add/', city_add, name="city_add"),
# CITY EDIT
   url(r'city_edit/(?P<c_id>\d+)/', city_edit),


# DOER
# ============================================================
# SEARCH
    url(r'search/', plot_search),
# DELETE
    url(r'plot/del/(?P<d_id>\d+)/', plot_del),
# EDIT
    url(r'plot/(?P<e_id>\d+)/', plot_edit, name="mapplot_edit"),
# MAIN & ADD NEW
    url(r'plot/', plot),

]
