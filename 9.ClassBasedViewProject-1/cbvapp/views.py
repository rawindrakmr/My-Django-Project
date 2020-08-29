from django.shortcuts import render
from  django.views.generic import View
from django.http import HttpResponse

# Create your views here.
class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1>This is from class based view</h1>')