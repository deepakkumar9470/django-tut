from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.
def show(request):
    fm=StudentRegistration()
    return render(request,'hello/hello.html',{'form':fm})