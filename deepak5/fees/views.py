from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def f_django(request):
   return render(request,'fees/hello2.html')