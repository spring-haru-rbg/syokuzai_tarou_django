
from django.urls import path
from . import views #追加


urlpatterns = [
    path('',views.refrigerator , name = 'refrigerator'),
   # path('food_register',views.food_register , name = 'food_register'),
    path('food_register',views.food_register , name = 'food_register'),
]
