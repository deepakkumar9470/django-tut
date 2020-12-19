# URL Dispatching and URL Patern


from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def my_django(request):
    return HttpResponse('<h1>My Name is Deepak Kumar</h1>')
