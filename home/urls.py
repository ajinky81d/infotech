

from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("temp_c",views.temp_c,name='temp_c'),
    path("calculator",views.calculator,name='calculator'),
     
     
]
