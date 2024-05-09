

from django.urls import path
from . import views



app_name = 'meals'

urlpatterns = [
    path('meal_list',views.meal_list , name='meal_list' ),

    path('<slug:slug>/' , views.meal_detail , name='meal_detail'),






]