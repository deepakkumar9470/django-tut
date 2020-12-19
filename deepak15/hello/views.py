# How to Get Data Form in Django
from django.shortcuts import render
from .forms import StudentRegistration
def show(request):
    if request.method=='POST':
        fm=StudentRegistration()

        if fm.is_valid:
            name=fm.changed_data['name']   
            email=fm.changed_data['email'] 
    else:
        fm=StudentRegistration()         
    return render(request,'hello/hello.html',{'form':fm})

    