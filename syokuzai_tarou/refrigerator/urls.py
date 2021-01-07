
from django.urls import path
from . import views #追加


urlpatterns = [
    path('',views.refrigerator , name = 'refrigerator'),
    path('food_register',views.food_register , name = 'food_register'),
    path('food_change_select',views.food_change_select , name = 'food_change_select'),
    path('food_search',views.food_search , name = 'food_search'),
    path('food_delete',views.food_delete , name = 'food_delete'),
    path('food_change/<int:num>',views.food_change , name = 'food_change'),
]
