from django.urls import path
from . import views #追加


urlpatterns = [
    path('',views.index , name = 'index'),
    path('home/',views.home , name = 'home'),
]