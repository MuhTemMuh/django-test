from django.urls import path
from . import views

urlpatterns = [
    path('<slug:catid>/', views.category, name='category_view'),
    path('about/', views.inform, name='inform'),
]


