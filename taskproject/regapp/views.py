from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def register(request):
    regsuccess=False
    msg=''
    uname=''
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
            return render(request, 'reg.html', {'msg': msg, 'regsuccess': regsuccess, 'uname': uname})
        elif User.objects.filter(email=email).exists():
            msg=f'Email {email} is already taken. use another email'
            messages.info(request,msg)
            print(msg)
            return render(request, 'reg.html', {'msg': msg, 'regsuccess': regsuccess, 'uname': uname})
        elif pwd1 != pwd2:
            msg = 'Passwords not matching'
            messages.info(request, msg)
            print(msg)
            return render(request, 'reg.html', {'msg': msg, 'regsuccess': regsuccess, 'uname': uname})
        else:
            user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pwd1)
            user.save()
            msg=f'User {uname} registered successfully'
            messages.info(request, msg)
            print(msg)
            regsuccess=True
            return render(request,'login.html',{'msg':msg,'regsuccess':regsuccess,'uname':uname})
    return render(request,'reg.html',{'msg':msg,'regsuccess':regsuccess,'uname':uname})

def login(request):
    loginsuccess,msg,uname=False,'',''
    if request.method=='POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        user=auth.authenticate(username=uname,password=pwd)
        if user is not None:
            auth.login(request,user)
            msg=f'User {uname} logged in successfully'
            loginsuccess=True
            messages.info(request, msg)
            print(msg)
            return render(request,'index.html',{'msg':msg,'loginsuccess':loginsuccess,'uname':uname})
        else:
            msg='invalid username or password'
            messages.info(request, msg)
            print(msg)
            return render(request,'login.html',{'msg':msg,'loginsuccess':loginsuccess,'uname':uname})
    return render(request, 'login.html', {'msg': msg, 'loginsuccess': loginsuccess, 'uname': uname})


def logout(request):
    logoutsuccess=True
    auth.logout(request)
    msg='logged out successfully'
    print(msg)
    return render(request, 'index.html', {'msg': msg, 'logoutsuccess': logoutsuccess})

