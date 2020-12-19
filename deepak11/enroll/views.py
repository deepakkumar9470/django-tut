# Django Form Creation
from django.shortcuts import render
from .forms import StudentRegistration


def show(request):
    fm=StudentRegistration(label_suffix='')
    return render(request,'enroll/info.html',{'form':fm})


