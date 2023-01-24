from django.shortcuts import render
from django.shortcuts import HttpResponse, render

# Create your views here.


def say_hello(request):
    return HttpResponse("Hello lol")


def home_screen(request):
    return render(request, "tinweb/home.html", {})
