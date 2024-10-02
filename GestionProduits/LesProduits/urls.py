from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    path("home", views.home, name="home"),
    #path("contact", views.contact, name="contact"),
    #path("about", views.about, name="about"),
    #path("home/<param>",views.accueil ,name='accueil'),
    #path("productview", views.listeProduits, name="lesProduits"),
    #path("itemview", views.listeDeclinaisons, name="lesDeclinaisons"),
    #path("productview/<id_produit>", views.detailProduit, name="detailProduit"),
    #path("home2", TemplateView.as_view(template_name="home2.html")),
    #path("home3", views.HomeView.as_view()),
    path("about", views.AboutView.as_view()),
    path("contact", views.ContactView, name="contact"),

    path("product/list",views.ProductListView.as_view(), name="product-list"),
    path("product/<pk>", views.ProductDetailView.as_view(), name="product-detail"),

    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),

    #path("product/add/",views.ProductCreate, name="product-add"),
    path("product/add/",views.ProductCreateView.as_view(), name="product-add"),
    path("product/<pk>/update/",views.ProductUpdateView.as_view(), name="product-update"),
    path("product/<pk>/delete/",views.ProductDeleteView.as_view(), name="product-delete"),
]