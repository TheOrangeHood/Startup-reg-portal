from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path('',views.index, name="home"),
    path('logout',views.logoutUser, name="logout"),
    path('login',views.loginUser, name="login"),
    path('form',views.regForm, name="form"),

]