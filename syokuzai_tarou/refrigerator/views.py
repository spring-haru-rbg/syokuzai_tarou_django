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
