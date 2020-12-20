from django import forms
from .models import *
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

# 食材登録フォーム(食材名)
class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['foodName']
        labels = {'foodName':'食材名',}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foodName'].widget.attrs['class'] = 'form-control'
        self.fields['foodName'].widget.attrs['placeholder'] = '食材名'

# 食材登録フォーム(FoodSet)
class FoodSetRegisterForm(forms.ModelForm):
    class Meta:
        model = FoodSet
        fields = ['foodGram','volume','limitRegister']
        labels = {'foodGram':'数量','volume':'数量の単位','limitRegister':'賞味・消費期限'}
        widgets = {
            'limitRegister': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['foodGram'].widget.attrs['class'] = 'form-control'
        self.fields['foodGram'].widget.attrs['placeholder'] = '量'
        self.fields['volume'].widget.attrs['class'] = 'form-control'
        self.fields['volume'].widget.attrs['placeholder'] = '単位'
        self.fields['limitRegister'].widget.attrs['class'] = 'form-control'
        self.fields['limitRegister'].widget.attrs['placeholder'] = '日付'

    # 数量が０以上かどうかチェックする
    def check_gram(self):
        foodGram = self.cleaned_data.get('foodGram')
        if value < 0:
            raise ValidationError("数量は0以上にしてください")
        return foodGram
    

# RegisterFormSet = forms.inlineformset_factory(
#     parent_model=Food,
#     model=FoodSet,
#     extra=1,
#     fields=("limitRegister", "foodGram", "volume", "food"),
#     #fields='__all__',
#     form=FoodSetRegisterForm
# )
 
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
        labels = {'foodGram':'',}

#　検索フォーム
class SearchForm(forms.Form):
    search = forms.CharField(label=False,required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['search'].widget.attrs['class'] = 'form-control'
        self.fields['search'].widget.attrs['placeholder'] = '食品名'
        