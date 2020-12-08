from django import forms
from .models import *
from .models import Food
from . import models
from django.contrib.admin import widgets
import bootstrap_datepicker_plus as datetimepicker
import os


#class FoodForm(forms.Form):
#    foodName = forms.CharField(label='foodName')


class SelectForm(forms.Form): 
    select = forms.ModelChoiceField(
        models.Food.objects,
        label='foodname',
        widget=forms.RadioSelect, 
        initial=0
        )

class CheckForm(forms.Form):
    delete = forms.ModelChoiceField(
        models.Food.objects,
        label='foodname',
        widget=forms.CheckboxInput,
        initial=0
    )

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['foodName']

class FoodSetForm(forms.ModelForm):
    class Meta:
        model = FoodSet
        
        fields = ['food','limitRegister','foodGram']
        widgets = {
            'limitRegister': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
        }