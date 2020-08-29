from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request,'generators/home.html')

def aboutus(request):
    return render(request, 'generators/aboutUs.html')


def password(request):
    length=int(request.GET.get('length',12))
    pass_cahr=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        pass_cahr.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        pass_cahr.extend(list('1234567890'))
    if request.GET.get('special'):
        pass_cahr.extend(list('! "#$%&()*+,‐./:;\'<=>?@'))
    password=''
    for char in range(length):
        password+=random.choice(pass_cahr)
    return render(request, 'generators/password.html', {'password':password})

