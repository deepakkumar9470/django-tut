from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def variable(request):
    a='<h1>My Name is Deepak Kumar Chouhan</h1>'
    b='<h1>My Name is Suraj Kumar , I am brother of Deepak Kumar Chouhan</h1>'
    return HttpResponse(a+' '+b)
