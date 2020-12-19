
# Models and Show or Retrieve Database Table Data to User
from django.shortcuts import render
from .models import Student 


def student_info(request):
    stud=Student.objects.all()
    return render(request,'enroll/student.html',{'stu':stud})