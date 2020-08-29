from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=35)
    rollno=models.IntegerField()
    marks=models.IntegerField()