from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    return HttpResponse("<h3>Hello, world!</h3>")
