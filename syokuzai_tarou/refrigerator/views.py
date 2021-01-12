from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.shortcuts import redirect
#from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.



@login_required
def refrigerator(request):
    foods = Refrigerator.objects.filter(user=request.user).order_by('foodset').reverse()
    header = ['食材名','数量','賞味・消費期限']
    params = {
        'title' : '食材残さないよ太郎',
        'text' : 'レシピを表示する際に使いたい食材にチェックを入れてレシピ表示ボタンを押してください',
       
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
        'foods' : foods,
        'header': header
    }
    return render(request, 'refrigerator/refrigerator.html',params)

@login_required
def food_register(request):
    params = {
        'title' : '食材登録',
        'text' : 'ここを食材登録に変更してね',
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
        'messgage' : '',
        'form_food' : FoodForm(),
        'form_foodset' : FoodSetRegisterForm(),
        
    }
    if request.method == 'POST':
        obj = FoodSet()
        obj2 = Food()
        foodset_form = FoodSetRegisterForm(request.POST, instance=obj)
        food_form = FoodForm(request.POST, instance=obj2)

        if food_form.is_valid():
            food_form.save()

        foodID_list = Food.objects.filter(foodName=request.POST.get('foodName')).values_list('id', flat=True)
        food_id = foodID_list[0]
        food = Food.objects.get(id=food_id)

        foodset_field = FoodSet.objects.create(food=food, limitRegister=request.POST.get('limitRegister'), foodGram=request.POST.get('foodGram'), volume=request.POST.get('volume'))
        foodset_field.save()
        refrigerator = Refrigerator.objects.create(user=request.user,foodset=foodset_field)
        refrigerator.save()
        # 登録完了メッセージ
        messages.success(request, '食材登録しました。')
    return render(request, 'refrigerator/food_register.html',params)

@login_required
def food_change_select(request):
    header = ['食材名','数量','賞味・消費期限']
    foods = Refrigerator.objects.filter(user=request.user).order_by('foodset').reverse()
    #POST送信時の処理
    if (request.method == 'POST'):
     #Foodsのチェック更新時の処理
        
        checks_value = request.POST.getlist('foods')
        for item in checks_value:
            change_data = Refrigerator.objects.get(id=item) 
            num = item
       
        return redirect(to='/refrigerator/food_change/'+num)
            
    #GETアクセス時の処理
    else:
        #フォームの用意
        selectform = SelectForm(request.user,foods=foods)
        for field in selectform:
                foodlist = zip(field,foods)

    params = {
        'title' : '食材変更',
        'text' : '変更ページ',
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
        'select_form' : selectform,
        'header' : header,
        'foodlist' : foodlist,
    }
    
    return render(request, 'refrigerator/food_change_select.html',params)

@login_required
def food_change(request,num):
    foods = Refrigerator.objects.get(id=num).foodset.id
    foodset = FoodSet.objects.get(id=foods)
    if (request.method == 'POST'):
        change_foods = FoodGramChangeForm(request.POST, instance=foodset )
        change_foods.save()

        # 削除完了メッセージ
        messages.success(request, '食材変更しました。')
        return redirect(to='/refrigerator/food_change_select') 

    params = {
        'title' : '数量変更',
        'text' : '食材数量変更ページ',
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
        'goto_change_refrigerator' : 'refrigerator',
        'goto_change_refrigerator_text' : '数量変更',
        'id' : num,
        'form' : FoodGramChangeForm(instance=foodset),
        'foodset' : foodset,

    }
    return render(request, 'refrigerator/food_change.html',params)

@login_required
def food_search(request):
    header = ['食材名','数量','賞味・消費期限']
    if request.method == 'POST':
        form = SearchForm(request.POST)
        msg = '食品名を入れてください'
        search_name = request.POST['search']
        foods = Refrigerator.objects.filter(user=request.user).filter(foodset__food__foodName__icontains = search_name).order_by('foodset').reverse()
    else:
        form = SearchForm()
        foods = Refrigerator.objects.filter(user=request.user).order_by('foodset').reverse()
        msg = '食品名を入れてください'
    params = {
        'title' : '食材検索',
        'text' : '検索ページ',
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
        'header': header,
        'form' : form,
        'foods' : foods,
        'msg' : msg,

    }
    return render(request, 'refrigerator/food_search.html',params)


@login_required
def food_delete(request):
    foods = Refrigerator.objects.filter(user=request.user).order_by('foodset').reverse()
    header = ['食材名','数量','賞味・消費期限']
    #POST送信時の処理
    if (request.method == 'POST'):
     #Foodsのチェック更新時の処理
        
        checks_value = request.POST.getlist('foods')
        for item in checks_value:
            delete_data = Refrigerator.objects.get(id=item) 
            delete_data.delete()
        foodsform = FoodsForm(request.user,foods=foods)
        for field in foodsform:
            foodlist = zip(field,foods)
        # 削除完了メッセージ
        messages.success(request, '食材削除しました。')
       # return redirect(to='refrigerator/food_delete')
            
    #GETアクセス時の処理
    else:
        #フォームの用意
        foodsform = FoodsForm(request.user,foods=foods)
        for field in foodsform:
                foodlist = zip(field,foods)
    params = {
        'title' : '削除',
        'text' : '削除ページ',
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
        #'goto_delete_refrigerator' : 'refrigerator',
        #'goto_delete_refrigerator_text' : '食材削除',
        #checkbox
        'foods_form' : foodsform,
        'foods' : foods,
        'header': header,
        'foodlist' : foodlist,    
    }
    
    return render(request, 'refrigerator/food_delete.html',params)


