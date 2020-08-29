from django.contrib import admin
from studentRegapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=['name', 'marks','rollno']


admin.site.register(Student,StudentAdmin)