from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("home/<param>",views.accueil ,name='accueil'),
    path("productview", views.listProduits, name="lesProduits"),
]