# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm
)
from accounts.models import  CustomUser

# ログインフォーム  
class LoginForm(AuthenticationForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'お名前'
    self.fields['password'].widget.attrs['class'] = 'form-control'
    self.fields['password'].widget.attrs['placeholder'] = 'パスワード'
    # for field in self.fields.values():
    #   field.widget.attrs['class'] = 'form-control'    
    #   field.widget.attrs['placeholder'] = field.label 

# 新規作成フォーム
class RegisterForm(UserCreationForm):
 
  # 入力を必須にするため、required=Trueで上書き
  username = forms.CharField(required=True)
 
  class Meta:
    model = CustomUser
    fields = ['username', 'password1', 'password2']
    # labels = {'username':'ユーザー名','password1':'パスワード','password2':'パスワード（もう一度入力してください）'}
    
 
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
 
    self.fields['username'].widget.attrs['class'] = 'form-control'
    self.fields['username'].widget.attrs['placeholder'] = 'お名前'
 
    self.fields['password1'].widget.attrs['class'] = 'form-control'
    self.fields['password1'].widget.attrs['placeholder'] = 'パスワード'
  
    self.fields['password2'].widget.attrs['class'] = 'form-control'
    self.fields['password2'].widget.attrs['placeholder'] = 'パスワード（もう一度入力してください）'

# パスワード変更フォーム
class MyPasswordChangeForm(PasswordChangeForm):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['old_password'].widget.attrs['class'] = 'form-control'
    self.fields['old_password'].widget.attrs['placeholder'] = '元のパスワード'
    self.fields['new_password1'].widget.attrs['class'] = 'form-control'
    self.fields['new_password1'].widget.attrs['placeholder'] = '新しいパスワード'
    self.fields['new_password2'].widget.attrs['class'] = 'form-control'
    self.fields['new_password2'].widget.attrs['placeholder'] = '新しいパスワード（もう一度入力してください）'