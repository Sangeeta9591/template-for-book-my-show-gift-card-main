from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from optparse import Option
from django.contrib import auth
from django.contrib.auth import authenticate


# Create your views here.
def login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        psword=request.POST.get('password')

        user=auth.authenticate(Username=uname,password=psword,)
        
        print('logged in')
        return redirect('/query.html')
        if user is not None:
            auth.login(request,User)
        else:
            return render(request, 'signup.html')
    else:
        return render(request, 'signup.html')
def signup(request):
    if request.method=='POST':
        
        username=request.POST.get('Username')
        password=request.POST.get('password')
        
        user=User.objects.create_user(username=username,password=password,)
    
        print('account created')
        return redirect('/')
    else:
        return render(request, 'signup.html')
def index(request):
    return render(request, 'index.html')
def admin(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('psword')

        user=authenticate(username='admin',password='12345',)
        
        print('admin logged in')
        return render(request, 'index.html')
        
    else:
        return render(request, 'admin.html')
def about(request):
    return render(request, 'aboutus.html')
def query(request):
    return render(request, 'query.html')


def contact(request):
    return render(request, 'contact.html')