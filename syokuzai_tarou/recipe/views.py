from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from refrigerator.models import *

# Create your views here.

@login_required
def recipe_select(request):
    foods = Refrigerator.objects.filter(user=request.user).order_by('foodset').reverse()
    header = ['食材名']
    #POST送信時の処理
    if (request.method == 'POST'):
     #Foodsのチェック更新時の処理
        checks_value = request.POST.getlist('foods')
        for item in checks_value:
            recipe_data = Refrigerator.objects.get(id=item) 
        return redirect(to='/recipe')
            
    #GETアクセス時の処理
    else:
        #フォームの用意
        foodsform = RecipeForm(request.user,foods=foods)
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
        #checkbox
        'foods_form' : foodsform,
        'foods' : foods,
        'header' : header,
        'foodlist' : foodlist,
    }
    return render(request, 'recipe/recipe_select.html',params)

@login_required
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
    return render(request, 'recipe/recipe.html',params)