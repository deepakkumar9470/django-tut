from django.shortcuts import render

# Create your views here.
def f_django(request):
   course='Python'
   duration='3 Months'
   reference='Udemy.com'
   coursename={'cname':course,'du':duration,'ref':reference}
   return render(request,'fees/hello2.html',coursename)