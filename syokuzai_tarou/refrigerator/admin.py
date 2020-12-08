from django.contrib import admin

# Register your models here.

#from .models import Food
from .models import *

admin.site.register(Food)
admin.site.register(FoodSet)
admin.site.register(Refrigerator)