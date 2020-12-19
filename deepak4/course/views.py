#URL Dispatcher or URL Pattern inside Application in Django


from django.http import HttpResponse
# Create your views here.
def c_django(request):
    return HttpResponse('<h1>My Name is Deepak Kumar</h1>')
def c_javascript(request):
    return HttpResponse('<h2>I have done Javascript</h2>')
