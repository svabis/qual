# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from .views import mapplot_admin
from .views import city_add, city_edit
from .views import city_export_xls

from .views import city_export_pdf #, city_export_html

from .views import city_select

from .views import plot, plot_edit, plot_del, plot_search


urlpatterns = [
# ADMIN
# ============================================================
# ADMIN VIEW
   url(r'admin/', mapplot_admin),

# CITY ADD
   url(r'city_add/', city_add, name="city_add"),
# CITY EDIT
   url(r'city_edit/(?P<c_id>\d+)/', city_edit),

# CITY DATA EXCEL EXPORT
   url(r'city_export_xls/(?P<c_id>\d+)/', city_export_xls),

# CITY DATA PDF EXPORT
   url(r'city_export_pdf/(?P<c_id>\d+)/', city_export_pdf),
#   url(r'city_export_pdf_html/(?P<c_id>\d+)/', city_export_html),



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


# DOER CITY SELECT
    url(r'', city_select),

]
