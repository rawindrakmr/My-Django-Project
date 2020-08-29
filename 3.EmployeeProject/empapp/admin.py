from django.contrib import admin
from empapp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['emp_no','emp_name','emp_salary','emp_address']

admin.site.register(Employee,EmployeeAdmin)
