from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.loginUsuario, name="loginUsuario"),
    path("logout/", views.logoutUsuario, name="logoutUsuario"),
]