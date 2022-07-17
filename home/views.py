from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from home.models import startUp
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method=="POST":
         username = request.POST.get('username')
         password = request.POST.get('password')
         print(username, password)

        # check if user has entered correct credentials
         user = authenticate(username=username, password=password)

         if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

         else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def regForm(request):
    # if request.user.is_authenticated:
    if request.method=="POST":
        name = request.POST.get('name')
        contactNo = request.POST.get('contact')
        email = request.POST.get('email')
        iitian = request.POST.get('IITian')
        hostel = request.POST.get('hostel')
        startup_name = request.POST.get('startupname')
        startup_sector = request.POST.get('sector')
        startup_desc = request.POST.get('desc')
        comments = request.POST.get('comments')
        ins = startUp(name = name, contactNo = contactNo, email = email,iitian = iitian, hostel = hostel,  startup_name = startup_name, startup_sector = startup_sector,  startup_desc = startup_desc, comments = comments)
        ins.save()
        print("The startup has been added")
        
    return render(request, 'form.html')