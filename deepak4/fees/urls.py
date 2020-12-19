from django.urls import path
from . import views
urlpatterns =[
    path('f1/',views.f_django),
    path('f2/',views.f_javascript),
]