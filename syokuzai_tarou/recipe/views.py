from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from refrigerator.models import *
from bs4 import BeautifulSoup    # importする
import urllib.request
import requests
import urllib.parse
from django.shortcuts import redirect
from urllib.parse import quote
from urllib.parse import unquote
from urllib.parse import urlencode
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
import re

# Create your views here.

@login_required
def recipe_select(request):
    foods = Refrigerator.objects.filter(user=request.user).order_by('foodset').reverse()
    header = ['食材名','数量','賞味・消費期限']
    #POST送信時の処理
    if (request.method == 'POST'):
     #Foodsのチェック更新時の処理
        checks_value = request.POST.getlist('foods')
        recipe = []
        for item in checks_value:
            recipe_data = Refrigerator.objects.get(id=item)
            recipe.append(recipe_data.foodset.food.foodName)
        # URLにパラメータを付与する
        recipe = {'param1':recipe}
        recipe = urllib.parse.urlencode(recipe)
        redirect_url = reverse('recipe')
        url = f'{redirect_url}?{recipe}'
        return redirect(url)
            
    #GETアクセス時の処理
    else:
        #フォームの用意
        foodsform = RecipeForm(request.user,foods=foods)
        for field in foodsform:
                foodlist = zip(field,foods)
    params = {
        'title' : 'レシピ表示',
        'text' : 'レシピ表示ページ',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '食材登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '食材変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '食材検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '食材削除',
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
    param1 = request.GET.get('param1') # param1の値を取得
    if (request.method == 'POST'):
        return redirect(to='/recipe/recipe_select')
    else:
        param1 = param1.replace('[','')
        param1 = param1.replace(']','')
        param1 = param1.replace(',','')
        param1 = param1.replace('\'','')
        param = urllib.parse.quote(param1)
        url = 'https://erecipe.woman.excite.co.jp/search/'+param
        #スクレイピング
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)

        # 全てのaタグを抽出
        recipe = soup.find_all('a' ,class_='recipename')
    
        links=[]
        recipe_names=[]
        for link in recipe:
            url_link = 'https://erecipe.woman.excite.co.jp' + link.get('href')
            links.append(url_link)
            recipe_names.append(link.get_text())


        #全てのdiv class＝"inner posrltv"を抽出

        recipe_image = []
        images = soup.find_all('img', class_='thmb fl lazy')
        for image in images:
            recipe_image.append(image.get('data-src'))
        link_list = zip(recipe_names,links,recipe_image)
    

    params = {
        'title' : 'レシピ検索結果表示',
        'text' : 'レシピ検索結果表示ページ',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '食材登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '食材変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '食材検索',
        'goto_recipe_select' : 'recipe_select',
        'goto_recipe_select_text' : 'レシピ表示',
        'goto_delete' : 'food_delete',
        'goto_delete_text' : '食材削除',
        'goto_recipe' : 'recipe',
        'goto_recipe_text' : 'レシピ検索',
        'goto_recipe_reselect' : 'recipe_select',
        'goto_recipe_reselect_text' : 'レシピ検索し直す',
        'links' : links,
        'name' : recipe_names,
        'link_list' : link_list,
        'param1' : param1,
    }
    return render(request, 'recipe/recipe.html',params)