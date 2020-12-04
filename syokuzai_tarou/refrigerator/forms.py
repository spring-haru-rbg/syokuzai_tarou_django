from django import forms
from .models import Food

class FoodForm(forms.Form):
    foodName = forms.CharField(label='foodName')