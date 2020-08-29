from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def datetime1(request):
    currentdatetime=datetime.datetime.now()
    msg='<h1>Hello Guest!!!Very very Good... '
    h=int(currentdatetime.strftime('%H'))
    if (h<12):
        msg+='<em>Morning<em></h1>'
    elif (h >=12 and h <16) :
        msg+='<em>Afternoon<em><h1>'
    elif (h >=16 and  h <=17):
        msg+='<em>Evening<em><h1>'
    else:
        msg+='<em>Good Night<em><h1>'
    return HttpResponse(msg +'current date and time is '+str(currentdatetime))
