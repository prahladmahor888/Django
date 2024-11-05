from django.contrib import admin
from django.urls import path
#from sqlalchemy.dialects.mssql.information_schema import views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="home"),
    path('docs', views.docs, name="docs"),
    path('example', views.examples, name="example"),
    path('reset', views.reset_pass, name="reset"),
    path('login', views.user_login, name="login"),
    path('signup', views.user_register, name="Signup"),
    path('logout', views.user_logout, name="logout"),
    path('new_pass', views.new_pass, name="New Password")
]