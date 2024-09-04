from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.home),
    path('home/<name>', views.home, name='home'),
]