#from django import forms
from .models import Food
from .models import *
#from django.contrib.admin import widgets

from django import forms
from django.contrib.admin import widgets
import os
from . import models


#class FoodForm(forms.Form):
#    foodName = forms.CharField(label='foodName')

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['foodName']


class SelectForm(forms.Form):
    select = forms.ModelChoiceField(models.Food.objects, label=Food.foodName, widget=forms.RadioSelect, initial=0)


#CHOICES = [(item.foodName) for item in Food.objects.all()]
#CHOICES =  {(item.id, item.foodName) for item in Food.objects.all()}


#{
 #   ('0','キュート'),
  #  ('1','クール'),
   # ('2','パッション'),
#}

#class SelectForm(forms.Form):
    #select = forms.ChoiceField(label='属性', widget=forms.RadioSelect, choices= CHOICE, initial=0)