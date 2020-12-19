from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def family(request):
    a='<h1>My Name is Deepak Kumar Chouhan</h1>'
    b='<h1>My Mother name is Manti Devi</h1>'
    return HttpResponse(a+' '+b)


