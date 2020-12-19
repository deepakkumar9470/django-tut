from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def f_django(request):
    return HttpResponse('<h1>My Name is Deepak Kumar</h1>')
def f_javascript(request):
    return HttpResponse('<h2>I am Learning Django </h2>')
