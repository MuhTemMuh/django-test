"""
URL configuration for MTM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import category, index
from MTM import settings
from django.conf.urls.static import static
from myapp import views
from myapp.views import show_post, show_category


urlpatterns = [
    path('admin/', admin.site.urls), 
    # path('categories/<slug:catid>/', view=category),
    path('inform/', views.inform, name='inform'), 
    path('news/', views.news, name='news'), 
    path('index/', views.index, name='home'), 
    path('', index, name='index'),
    path('Posts/',views.news, name='posts'),
    path('news_today/',views.news_today, name='news_today'),
    path('Posts/',views.news_today, name='posts'),
    path('car/', views.car, name='car'),
    path('merc/', views.merc, name='merc'),
    path('nedviga/',views.nedviga,name='nedviga'),
    path('real/',views.real, name='real'),
    path('Login/',views.Login, name='Login'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:category_id>/', show_category, name='category'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
