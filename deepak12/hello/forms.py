from django import forms

class StudentRegistration(forms.Form):
    # name=forms.CharField(label='Your Name', label_suffix=' ',initial='Deepak',    disabled=True,help_text='Limit no exceed more than 40 characters')

    name=forms.CharField(widget=forms.FileInput)