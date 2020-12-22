
from django.urls import path
from . import views #追加


urlpatterns = [
    path('',views.recipe , name = 'recipe'),
    path('recipe_select',views.recipe_select , name = 'recipe_select'),
    path('sample',views.sample, name='sample'),
    path('sample2',views.sample2 , name='sample2'),
]
