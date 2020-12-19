from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('Home Page')
def my_django(request):
    return HttpResponse('<h1>My Name is Deepak Kumar</h1>')