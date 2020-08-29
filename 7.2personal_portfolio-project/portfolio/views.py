from django.shortcuts import render
from portfolio.models import Project

# Create your views here.
def home(request):
    project_obj=Project.objects.all()
    return render(request,'portfolio/home.html',{'projects':project_obj})
