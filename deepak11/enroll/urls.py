from django.urls import path
from . import views
urlpatterns = [
    path('fm/', views.show),
]
