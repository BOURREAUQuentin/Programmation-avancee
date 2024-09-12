from django.shortcuts import render
from django.http import HttpResponse
from LesProduits.models import Product

def home(request):
    return HttpResponse("Bienvenue sur l'accueil")

def hello(request, name = ""):
    return HttpResponse("<h1>Bonjour " + name + " content de vous revoir ici !</h1>")

def list_products(request):
    produits = Product.objects.all()
    reponse = "<h1>Mes produits</h1> <ul>"
    for produit in produits:
        reponse += "<li>" + produit.name + " au prix de " + produit.price_ht.__str__() + "€</li>"
    reponse += "</ul>"
    return HttpResponse(reponse) 