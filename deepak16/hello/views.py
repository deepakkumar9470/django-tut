# Custom Path Converters
from django.shortcuts import render

def show(request,day):
    student={'dd':day}    
    return render(request,'hello/hello.html',student)

    