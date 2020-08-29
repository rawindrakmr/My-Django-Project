from django.shortcuts import render,redirect
from studentRegapp import forms

# Create your views here.
def register(request):
    form=forms.StudentForm()
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('register')
    return render(request,'studentRegapp/reg.html',{'form':form})
