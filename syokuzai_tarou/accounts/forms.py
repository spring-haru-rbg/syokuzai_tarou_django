# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import  CustomUser
    
class RegisterForm(UserCreationForm):
 
  # 入力を必須にするため、required=Trueで上書き
  username = forms.CharField(required=True)
  game_status = forms.IntegerField(required=False)
 
 
  class Meta:
    model = CustomUser
 
    fields = (
      "username", "password1", "password2", 
    )
    
 
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
 
    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'お名前'
 
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['placeholder'] = 'パスワード'
  
    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['placeholder'] = 'パスワード（確認）'