from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,People
# Create your views here.

def index(request):
    allpix=Place.objects.all()
    allppl=People.objects.all()
    return render(request,'index.html',{'allpix':allpix,'allppl':allppl})


def about(request):
    sss=['Bharat Mata ki jai',  'Using Jinja']
    return render(request,'about.html',{'abc':sss})
def contact(request):
    return HttpResponse('contact is here')
def details(request):
    return render(request,'details.html')
def thanks(request):
    return HttpResponse('thanks is here')
def form(request):
    return render(request,'form.html')
def operations(request):
    a = int(request.GET['a'])
    b = int(request.GET['b'])
    return render(request,'result.html',\
                  {'add':a+b,'sub':a-b,'mul':a*b,'div':a/b,'a':a,'b':b})

