from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
#User is for Register purpose and auth for login and permissions
# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']


        if password1==password2:
            if User.objects.filter(username=username).exists():#if user already exist
                messages.info(request, 'User name taken please choose others')
                #you can also use messages.error()
                return redirect('register')
            elif User.objects.filter(email=email).exists():#checking the email if alredy exist
                messages.info(request,'email already register with us')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,'password not matched')
            return redirect('register')
    
        
    else:
        return render(request, 'register.html')


#login
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')


#logout
def logout(request):
    auth.logout(request)
    return redirect('/')

    
