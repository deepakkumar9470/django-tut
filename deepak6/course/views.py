#Dynamic Template Files using DTLs
# Create your views here.
from django.shortcuts import render

def c_django(request):
     course='Django'
     duration='3 Months'
     reference='Udemy.com'
     coursename={'cname':course,'du':duration,'ref':reference}
     return render(request,'course/hello1.html',coursename)
     


