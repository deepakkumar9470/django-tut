from django import forms
from django.core import validators
class StudentRegistration(forms.Form):
     name=forms.CharField(error_messages={'Enter Your Name'})
     email=forms.EmailField(error_messages={'Enter Your Email'})
     password=forms.CharField(widget=forms.PasswordInput)
     

      
     




     