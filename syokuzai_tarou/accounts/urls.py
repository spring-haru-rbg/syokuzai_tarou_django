from django.urls import path
from . import views #追加


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', views.Login.as_view(), name='login'),
    path('password_change/', views.PasswordChange.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDone.as_view(), name='password_change_done'), #追加
]