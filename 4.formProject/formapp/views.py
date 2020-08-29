from django.shortcuts import render
from formapp import forms
# Create your views here.
def RegForm(request):
    form=forms.StudentForm()
    return render(request,'formapp/input.html',{'form':form})