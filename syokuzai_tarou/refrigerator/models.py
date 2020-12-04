from django.db import models

# Create your models here.

class Food(models.Model):
    foodName = models.CharField(max_length=20) #食材名
