from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_products, name='home'),
    path('home/<name>', views.hello, name='hello'),
]