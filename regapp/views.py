from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    if request.method=='POST':
        uname = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pwd1 = request.POST["password1"]
        pwd2 = request.POST["password2"]
        if User.objects.filter(username=uname).exists():
            msg=f'Username {uname} is already taken. use another Username'
            messages.info(request,msg)
            print(msg)
            return redirect('reg')
        elif User.objects.filter(email=email).exists():
            msg=f'Email {email} is already taken. use another email'
            messages.info(request,msg)
            print(msg)
            return redirect('reg')
        elif pwd1 != pwd2:
            msg = 'Passwords not matching'
            messages.info(request, msg)
            print(msg)
            return redirect('reg')
        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pwd1)
            user.save()
            msg=f'User {uname} Created successfully'
            messages.info(request, msg)
            print(msg)
            return redirect('login')
    return render(request,'reg.html')

def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            msg=f'User {uname} logged in successfully'
            messages.info(request, msg)
            print(msg)
            return render(request,'indexlogin.html')
        else:
            msg='invalid credentials'
            messages.info(request, msg)
            print(msg)
            return redirect('login')
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    print('logged out')
    return render(request, 'indexlogin.html')