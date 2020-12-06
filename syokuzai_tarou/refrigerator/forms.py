from django import forms
#from .models import Food
from .models import *
<<<<<<< HEAD
import bootstrap_datepicker_plus as datetimepicker
=======
>>>>>>> master

#class FoodForm(forms.Form):
#    foodName = forms.CharField(label='foodName')

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['foodName']

<<<<<<< HEAD
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
=======
>>>>>>> master
