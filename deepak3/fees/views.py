from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_js(request):
    return HttpResponse('<h1>I am Learning Rest API now in morning</h1>')

