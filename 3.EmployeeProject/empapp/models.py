from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_no=models.IntegerField()
    emp_name=models.CharField(max_length=250)
    emp_salary=models.FloatField()
    emp_address=models.CharField(max_length=250)
