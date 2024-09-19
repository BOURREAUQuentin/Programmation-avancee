from django.shortcuts import render
from django.http import HttpResponse
from LesProduits.models import Product, ProductItem

# def home(request):
#     return HttpResponse("Bienvenue sur l'accueil")

# def hello(request, name = ""):
#     return HttpResponse("<h1>Bonjour " + name + " content de vous revoir ici !</h1>")

# def list_products(request):
#     produits = Product.objects.all()
#     reponse = "<h1>Mes produits</h1> <ul>"
#     for produit in produits:
#         reponse += "<li>" + produit.name + " au prix de " + produit.price_ht.__str__() + "€</li>"
#     reponse += "</ul>"
#     return HttpResponse(reponse)

def home():
    return HttpResponse("<h1>Hello Django!</h1>")

def about(request):
    return render(request, 'LesProduits/about.html')

def contact(request):
    return render(request, 'LesProduits/contact.html')

def accueil(request,param):
    return HttpResponse("<h1>Hello " + param + " ! You're connected</h1>")

def listeProduits(request):
    prdcts = Product.objects.all()
    return render(request, 'LesProduits/list_products.html', {'prdcts': prdcts})

def listeDeclinaisons(request):
    declinaisons = ProductItem.objects.all()
    return render(request, 'LesProduits/list_items.html', {'liste_declinaisons': declinaisons})

def detailProduit(request,id_produit):
    # gérer cas d'erreur
    produitRecherche = Product.objects.all().filter(code=id_produit)
    print(produitRecherche)
    return render(request, 'LesProduits/detail_product.html', {'produit': produitRecherche})

# faire vue pour id d'un produit et si ca existe pas on renvoi erreur 404