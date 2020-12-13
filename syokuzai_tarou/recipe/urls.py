
from django.urls import path
from . import views #追加


urlpatterns = [
    path('',views.recipe , name = 'recipe'),
    path('recipe_select',views.recipe_select , name = 'recipe_select'),
]
