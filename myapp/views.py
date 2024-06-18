from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from myapp.models import *
from myapp.models import Posts, Category

# Create your views here.

menu=["О нас","Новости","Новости дня","Login","Sign-Up"]
def category(request,catid):
    return HttpResponse(f"Вы на странице категории {catid}")

def index(request):
    all_posts=Posts.objects.all()
    categ=Category.objects.all()
    return render(request, 'home.html',{'title':'Наш Блог','menu':menu,'category':category, 'all':all_posts, 'categ': categ})
def inform(request):
    return render(request, 'inform.html',{'posts':Posts})
def news(request):
    posts=Posts.objects.all()
    return render(request,'news.html',{'posts':posts})
def news_today(request):
    posts=Posts.objects.all()
    return render(request, 'news_today.html',{'posts':posts})
def car(request):
    return render(request, 'car.html')
def merc(request):
    return render(request, 'merc.html')
def nedviga(request):
    return render(request, 'nedviga.html')
def real(request):
    return render(request, 'real.html')
def Login(request):
    return render(request, 'Login.html')
def Sign_Up(request):
    return render(request, 'Sign_Up.html')
def archieve(request):
    return HttpResponse("catid")

from django.shortcuts import render, get_object_or_404
from .models import Posts, Category

def show_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    categ = Category.objects.all()
    return render(request, 'app/post.html', {
        'title': post.title,
        'menu': menu, 
        'post': post,  
        'categ': categ
    })

def show_category(request, category_id):
    # return HttpResponse(f"Категория под номером {category_id}")

    all_posts = Posts.objects.filter(categoria_id=category_id)
    categ = Category.objects.all()
    return render(request, 'home.html', {'title': 'Главная страница', 'menu': menu, 'all': all_posts, 'categ': categ})