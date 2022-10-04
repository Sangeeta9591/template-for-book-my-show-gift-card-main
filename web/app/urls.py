from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('signup.html',views.signup),
    path('login',views.login),
    path('signup',views.index),
    path('aboutus.html',views.about),
    path('query.html',views.query),
   
    path('contact.html',views.contact),
    
]