from django import forms
from .models import *
from .models import Food
from . import models
from django.contrib.admin import widgets
import bootstrap_datepicker_plus as datetimepicker
from django.core.exceptions import ValidationError
import os
from django.forms import inlineformset_factory



#radio
class SelectForm(forms.Form): 
    def __init__(self, user, foods=[], *args, **kwargs ):
        super(SelectForm, self).__init__(*args,**kwargs)
        self.fields['foods'] = forms.ChoiceField(
            label = "",
            choices = [(item.id,item.foodset) for item in foods],
            widget = forms.RadioSelect(),
            initial = 0
        )

# delete_checkbox 食材削除チェックボックス
class FoodsForm(forms.Form):
    def __init__(self, user, foods=[], *args, **kwargs ):
        super(FoodsForm, self).__init__(*args,**kwargs)
        self.fields['foods'] = forms.MultipleChoiceField(
            label = "",
            choices = [(item.id,item.foodset) for item in foods],
            widget = forms.CheckboxSelectMultiple(),
            initial = 0
        )

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['foodName']

# 食材登録フォーム
class FoodSetRegisterForm(forms.ModelForm):
    class Meta:
        model = FoodSet
        
        fields = ['food','limitRegister','foodGram','volume']
        widgets = {
            'limitRegister': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
        }
    # 数量が０以上かどうかチェックする
    def check_gram(self):
        foodGram = self.cleaned_data.get('foodGram')
        if value < 0:
            raise ValidationError("数量は0以上にしてください")
        return foodGram

RegisterFormSet = forms.inlineformset_factory(
    parent_model=Food,
    model=FoodSet,
    extra=1,
    fields=("limitRegister", "foodGram", "volume", "food"),
    #fields='__all__',
    form=FoodSetRegisterForm
)
 
    #def clean(self):
     #   cleaned_data = super().clean()
      #  name = cleaned_data.get('name')
       # nickname = cleaned_data.get('nickname')
        #if not (name or nickname):
         #   raise forms.ValidationError("名前かニックネームのどちらかを入力して下さい")
        #return cleaned_data

# 食材数量変更フォーム
class FoodGramChangeForm(forms.ModelForm):
    class Meta:
        model = FoodSet
        
        fields = ['foodGram']

#検索フォーム
class SearchForm(forms.Form):
    search = forms.CharField(label=False,required=False)
        