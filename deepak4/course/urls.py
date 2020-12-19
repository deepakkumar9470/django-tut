from django.urls import path
from . import views
urlpatterns =[
    path('c1/',views.c_django),
    path('c2/',views.c_javascript),
]
