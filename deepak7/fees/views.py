from django.shortcuts import render

# Create your views here.
def django(request):
    return render(request,'fees/main_info.html')