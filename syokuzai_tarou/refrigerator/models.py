from django.db import models
from accounts.models import CustomUser
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


# Create your models here.

# Foodクラス
class Food(models.Model):
    foodName = models.CharField(max_length=20, unique=True) #食材名

#FoodSetクラス
    def __str__(self):
        return self.foodName


# 数量が０以上かどうかチェックする
def check_gram(value):
    if value < 0:
        raise ValidationError("数量は0以上にしてください")

# FoodSetクラス
class FoodSet(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    limitRegister = models.DateField(
        verbose_name='賞味・消費期限',
        blank=True,
        null=True,
    )
    foodGram = models.IntegerField(default=0,validators=[check_gram])
    volume = models.CharField(default='個',max_length=10)#数量の単位
    def __str__(self):
        return str(self.food) 
        
    def str_limitRegister(self):
        return str(self.limitRegister)

    class Meta:
        ordering = ('-limitRegister',)

# Refrigeratorクラス
class Refrigerator(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    foodset = models.ForeignKey(FoodSet, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)  + " : "  + str(self.foodset)     