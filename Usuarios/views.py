from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.views import View

@login_required
def home(request):
    return HttpResponse("Usuario LOgeado")

class loginUsuario(View):

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return HttpResponse("Error")


def loginUsuario(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return HttpResponse("Error")

@login_required
def logoutUsuario(request):
    logout(request)
    return redirect('home')

class inquilinoView(DetailView):
    pass