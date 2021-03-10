# -*- coding: utf-8 -*-
from django.forms import ModelForm

from .models import MapPlot, MapPlotCity
from .models import MapPlotType

from django import forms


# ======================================================================================
class MapPlotForm(ModelForm):

    class Meta:
        model = MapPlot
        fields = ['mark', 'city', 'device', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3']

#        ordering = ['radio__name']

        widgets = {
            'mark': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),

            'city': forms.Select(attrs={'style':'display:none;'}),

            'lat': forms.TextInput(attrs={'class': 'form-control input-sm', 'readonly':'readonly', 'style':'width:30%;float:left;'}),
            'lon': forms.TextInput(attrs={'class': 'form-control input-sm', 'readonly':'readonly', 'style':'width:30%'}), #;float:left;'}),

            'device': forms.TextInput(attrs={'style':'display:none;'}),

#            'radio': forms.RadioSelect(attrs={'class': 'form-control'}),
            'radio': forms.RadioSelect(attrs={'class': 'form-check'}),

            'chk_1': forms.CheckboxInput(attrs={'class': 'form-control', 'style':'margin-left:0px;'}),
            'chk_2': forms.CheckboxInput(attrs={'class': 'form-control', 'style':'margin-left:0px;'}),
            'chk_3': forms.CheckboxInput(attrs={'class': 'form-control', 'style':'margin-left:0px;'}),
        }

#'date', 'mark', 'city', 'lat', 'lon', 'radio', 'chk_1', 'chk_2', 'chk_3'

# ======================================================================================
class MapPlotCityForm(ModelForm):
    class Meta:
        model = MapPlotCity
        fields = ['name', 'lat', 'lon', 'zoom']


        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),

            'lat': forms.TextInput(attrs={'class': 'form-control input-sm', 'readonly':'readonly', 'style':'width:40%;float:left;'}),
            'lon': forms.TextInput(attrs={'class': 'form-control input-sm', 'readonly':'readonly', 'style':'width:40%;float:left;'}),
            'zoom': forms.TextInput(attrs={'class': 'form-control input-sm', 'readonly':'readonly', 'style':'width:20%;float:left;'}),
        }
