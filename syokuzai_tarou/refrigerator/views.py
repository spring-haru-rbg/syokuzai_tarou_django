from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def refrigerator(request):
    params = {
        'title' : '食材残さないよ太郎',
        'text' : 'レシピを表示するときは使いたい食材にチェックを入れてレシピ表示ボタンを押してください',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',
        'goto_register' : 'food_register',
        'goto_register_text' : '登録',
        'goto_change_select' : 'food_change_select',
        'goto_change_select_text' : '変更',
        'goto_search' : 'food_search',
        'goto_search_text' : '検索',

    }
    return render(request, 'refrigerator/refrigerator.html',params)

def food_register(request):
    params = {
        'title' : '食材登録',
        'text' : 'aiueo',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',

    }
    return render(request, 'refrigerator/food_register.html',params)

def food_change_select(request):
    params = {
        'title' : '食材変更',
        'text' : '変更ページ',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',

    }
    return render(request, 'refrigerator/food_change_select.html',params)

def food_search(request):
    params = {
        'title' : '食材検索',
        'text' : '検索ページ',
        'goto_refrigerator' : 'refrigerator',
        'goto_refrigerator_text' : '食材一覧',

    }
    return render(request, 'refrigerator/food_search.html',params)

