from django.urls import path, register_converter
from . import views, converters
register_converter(converters.FourYearDigitConverter, 'dddd')
urlpatterns = [
    path('session/<dddd:day>/', views.show, name='ShowDetails')
]
