from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import *

# signup
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views import generic
from django.contrib.auth.views import (
    LoginView, LogoutView
)

# Create your views here.

class SignUp(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = "accounts/signup.html" 
    
    def get_success_url(self):
        return reverse('refrigerator')

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        login(self.request, user) # 認証
        self.object = user 
        return HttpResponseRedirect(self.get_success_url()) # リダイレクト

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = "accounts/password_change.html" 


class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'

class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'registration/login.html'
   
    