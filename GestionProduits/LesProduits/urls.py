from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path("home", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("home/<param>",views.accueil ,name='accueil'),
    path("productview", views.listeProduits, name="lesProduits"),
    path("itemview", views.listeDeclinaisons, name="lesDeclinaisons"),
    path("productview/<id_produit>", views.detailProduit, name="detailProduit"),
    path("home2", TemplateView.as_view(template_name="home2.html")),
    path("home3", views.HomeView.as_view()),
    path("about2", views.AboutView.as_view()),
    path("product/list",views.ProductListView.as_view()),
]