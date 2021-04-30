from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='index'),
    path("loginuser",views.loginuser,name='loginuser'),
    path("logoutuser",views.logoutuser,name='logoutuser'),
    path("create",views.create,name='create'),
    path("home",views.home,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contacts",views.contacts,name='contacts'),
    path("pay",views.pay,name='pay'),
    path("cart",views.cart,name='cart'),
]