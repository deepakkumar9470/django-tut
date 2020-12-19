#Form ,Form Field Arguments,Widgets
from django.shortcuts import render

from .forms import StudentRegistration

def show(request):
    fm=StudentRegistration()
    return render(request,'hello/hello.html',{'form':fm})