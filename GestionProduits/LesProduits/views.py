from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenue sur l'accueil")

def hello(request, name = ""):
    return HttpResponse("<h1>Bonjour " + name + " content de vous revoir ici !</h1>")