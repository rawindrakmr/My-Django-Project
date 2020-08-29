from django.shortcuts import render,redirect
from CRUDapp.models import Employee
from CRUDapp.forms import EmployeeForms

# Create your views here.
def retrive_view(request):
    emp_list=Employee.objects.all()
    return render(request,'CRUDapp/index.html',{'emp_list':emp_list})

def EmpCreateView(request):
    form=EmployeeForms()
    if request.method=='POST':
        form=EmployeeForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/retrive')
    return render(request,'CRUDapp/create.html',{'form':form})

def delete_view(request,id):
    emp_del=Employee.objects.get(id=id)
    emp_del.delete()
    return redirect('/retrive')

def update_view(request,id):
    emp_update=Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForms(request.POST,instance=emp_update)
        if form.is_valid():
            form.save()
        return redirect('/retrive')
    return render(request,'CRUDapp/update.html',{'emp_update':emp_update})