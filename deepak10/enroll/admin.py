from django.contrib import admin
from enroll.models import Student


class StudentAdmin(admin.ModelAdmin):
 list_disp=('stuid','stuname','stuemail','stupass')

admin.site.register(Student,StudentAdmin)