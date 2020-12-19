# Templates in Django(Root Project)

from django.shortcuts import render
from django.http import HttpResponse
def c_django(request):
    return render(request,'course/hello1.html')


def c_javascript(request):
    return HttpResponse('<h2>I have done Javascript</h2>')
