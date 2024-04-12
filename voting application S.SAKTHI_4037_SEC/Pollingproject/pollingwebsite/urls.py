from django.contrib import admin
from django.urls import path,include
from pollingwebsite import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.home1,name='login'),
    path('index/',views.index,name='index'),
]