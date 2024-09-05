from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/<name>', views.hello, name='hello'),
]