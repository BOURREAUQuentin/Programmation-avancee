from django.urls import path
from . import views
from django.views.generic import *

urlpatterns = [
    
    #path("contact", views.contact, name="contact"),
    #path("about", views.about, name="about"),
    #path("home/<param>",views.accueil ,name='accueil'),
    #path("productview", views.listeProduits, name="lesProduits"),
    #path("itemview", views.listeDeclinaisons, name="lesDeclinaisons"),
    #path("productview/<id_produit>", views.detailProduit, name="detailProduit"),
    #path("home2", TemplateView.as_view(template_name="home2.html")),
    #path("home3", views.HomeView.as_view()),
    path("home", views.home, name="home"),
    path("about", views.AboutView.as_view()),
    path("contact", views.ContactView, name="contact"),

    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),

    ##################### PRODUIT #########################
    path("product/list",views.ProductListView.as_view(), name="product-list"),
    path("product/<pk>", views.ProductDetailView.as_view(), name="product-detail"),

    path("product/add/",views.ProductCreateView.as_view(), name="product-add"),
    path("product/<pk>/update/",views.ProductUpdateView.as_view(), name="product-update"),
    path("product/<pk>/delete/",views.ProductDeleteView.as_view(), name="product-delete"),

    ##################### PRODUIT ATTRIBUTES #########################
    path("attribute/list",views.ProductAttributeListView.as_view(), name="attribute-list"),
    path("attribute/<pk>", views.ProductAttributeDetailView.as_view(), name="attribute-detail"),
    path("attribute/<pk>/update/",views.ProductAttributeUpdateView.as_view(), name="attribute-update"),
    path("attribute/<pk>/delete/",views.ProductAttributeDeleteView.as_view(), name="attribute-delete"),

    ##################### PRODUIT ITEMS #########################
    path("item/list",views.ProductItemListView.as_view(), name="item-list"),
    path("item/<pk>", views.ProductItemDetailView.as_view(), name="item-detail"),
    path("item/<pk>/update/",views.ProductItemUpdateView.as_view(), name="item-update"),
    path("item/<pk>/delete/",views.ProductItemDeleteView.as_view(), name="item-delete"),
]