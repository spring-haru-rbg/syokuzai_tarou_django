from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import RegisterForm

# signup
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from django.views import generic

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')


@login_required
def home(request):
    return render(request, 'accounts/home.html')

#class home(LoginRequiredMixin, generic.TemplateView):
  #  """メニュービュー"""
   # template_name = 'accounts/home.html'
#
 #   def get_context_data(self, **kwargs):
  #      context = super().get_context_data(**kwargs) # 継承元のメソッドCALL
   #     context["form_name"] = "top"
    #    return context

class SignUp(CreateView):
    model = CustomUser
    form_class = RegisterForm
    template_name = "accounts/signup.html" 
    
    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        login(self.request, user) # 認証
        self.object = user 
        return HttpResponseRedirect(self.get_success_url()) # リダイレクト

class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    success_url = reverse_lazy('password_change_done')
    template_name = "accounts/password_change.html" 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #継承元のメソッドcall
        context["form_name"] = "password_change"
        return context

class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'
   
    