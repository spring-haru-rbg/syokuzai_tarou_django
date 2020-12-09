from django.shortcuts import render
from django.http import HttpResponse

#from .forms import FoodForm
#from .models import Food
from .forms import *
from .models import *
from django.shortcuts import redirect

from django import forms
from django.shortcuts import redirect, render


# Create your views here.




def refrigerator(request):
    data = Food.objects.all()
    foods = Refrigerator.objects.all()
    params = {
        'title' : '食材残さないよ太郎',
        'text' : 'レシピを表示する際に使いたい食材にチェックを入れてレシピ表示ボタンを押してください',
       
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '削除',
        
        'data' : data,
        'foods' : foods,
    }
    return render(request, 'refrigerator/refrigerator.html',params)

def food_register(request):
    params = {
        'title' : '食材登録',
        'text' : 'ここを食材登録に変更してね',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '削除',
        'messgage' : '',
        #'form' : FoodForm(), # 1204追加
        'form_food' : FoodForm(),
        'form_foodset' : FoodSetRegisterForm(),
    }
    if request.method == 'POST':
        obj = FoodSet()
        foodset = FoodSetRegisterForm(request.POST, instance=obj)
        if foodset.is_valid():
            params['message'] = 'OK'
            foodset.save()
        else:
            params['message'] = 'まだ登録できません'
            foodset.add_error('foodGram','LOGIN_ID、またはPASSWORDが違います。')
        #return redirect(to='/refrigerator/food_register')
    return render(request, 'refrigerator/food_register.html',params)
  

def food_change_select(request):
    data = Food.objects.all()
    params = {
        'title' : '食材変更',
        'text' : '変更ページ',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '削除',

        'data' : data,
        'form' : SelectForm(),

    }
    
    return render(request, 'refrigerator/food_change_select.html',params)

def food_change(request):
    params = {
        'title' : '数量変更',
        'text' : '食材数量変更ページ',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '削除',
        'goto_change_refrigerator' : 'refrigerator',
        'goto_change_refrigerator_text' : '数量変更',

    }
    return render(request, 'refrigerator/food_change.html',params)

def food_search(request):
    params = {
        'title' : '食材検索',
        'text' : '検索ページ',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '削除',

    }
    return render(request, 'refrigerator/food_search.html',params)

def recipe_select(request):
    params = {
        'title' : 'レシピ表示',
        'text' : 'レシピ表示ページ',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '削除',
        'goto_recipe' : 'recipe',
        'goto_recipe_text' : 'レシピ検索',
    }
    return render(request, 'refrigerator/recipe_select.html',params)

def recipe(request):
    params = {
        'title' : 'レシピ検索結果表示',
        'text' : 'レシピ検索結果表示ページ',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '削除',
        'goto_recipe' : 'recipe',
        'goto_recipe_text' : 'レシピ検索',
        'goto_recipe_reselect' : 'recipe_select',
        'goto_recipe_reselect_text' : 'レシピ検索し直す',
    }
    return render(request, 'refrigerator/recipe.html',params)

def food_delete(request):
    data = Food.objects.all()
    foods = Refrigerator.objects.all()
    #POST送信時の処理
    if (request.method == 'POST'):
     #Foodsのチェック更新時の処理
        
        checks_value = request.POST.getlist('foods')
        for item in checks_value:
            delete_data = Refrigerator.objects.get(id=item) 
            delete_data.delete()
        return redirect(to='/refrigerator')
            
    #GETアクセス時の処理
    else:
        #フォームの用意
        foodsform = FoodsForm(request.user,foods=foods)

    params = {
        'title' : '削除',
        'text' : '削除ページ',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '削除',
        'goto_delete_refrigerator' : 'refrigerator',
        'goto_delete_refrigerator_text' : '食材削除',

        'data' : data,
        #checkbox
        'foods_form' : foodsform,
        
    }
    
    return render(request, 'refrigerator/food_delete.html',params)




def calender(request):
    params = {
        'form_food' : FoodForm(),
        'form_foodset' : FoodSetForm(),
    }
    if request.method == 'POST':
        obj = FoodSet()
        foodset = FoodSetForm(request.POST, instance=obj)
        foodset.save()
        return redirect(to='/refrigerator/calender')

    return render(request, 'refrigerator/calender.html',params)
