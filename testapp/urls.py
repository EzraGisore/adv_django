
from django.urls import path
from . import views

app_name = "testapp"

urlpatterns = [
    path('',views.home,name="home"),
    path('about', views.about, name="about"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register")
]
