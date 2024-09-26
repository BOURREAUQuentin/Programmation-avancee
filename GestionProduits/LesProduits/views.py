from django.shortcuts import render
from django.http import HttpResponse
from LesProduits.models import Product, ProductItem
from django.contrib.auth import *
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

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

def home(request):
    return render(request, 'LesProduits/home.html')

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


from django.views.generic import *

class HomeView(TemplateView):
    template_name = "LesProduits/home3.html"
    def post(self, request, **kwargs):
        return render(request, self.template_name)

class AboutView(TemplateView):
    template_name = "LesProduits/about.html"
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us..."
        return context
    def post(self, request, **kwargs):
        return render(request, self.template_name)

class ProductListView(ListView):
    model = Product
    template_name = "LesProduits/list_products2.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste des produits"
        context['prdcts'] = Product.objects.all()
        return context

    def get_queryset(self ) :
        return Product.objects.order_by("price_ttc")

class ProductDetailView(DetailView):
    model = Product
    template_name = "LesProduits/detail_product2.html"
    context_object_name = "product"
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail produit"
        context['product'] = Product.objects.all().filter(code=1234)
        return context

class ConnectView(LoginView):
    template_name = 'LesProduits/login.html'
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'LesProduits/home.html',{'titreh1':username})
        else:
            return render(request, 'LesProduits/register.html')

class RegisterView(TemplateView):
    template_name = 'LesProduits/register.html'
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'LesProduits/login.html')
        else:
            return render(request, 'LesProduits/register.html')

class DisconnectView(TemplateView):
    template_name = 'LesProduits/logout.html'
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)