from django.shortcuts import render

from django.http import HttpResponse

def home(request, name = ""):
    return HttpResponse("Bonjour depuis Django : " + name)