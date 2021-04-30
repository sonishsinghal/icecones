from django.shortcuts import render,HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login ,logout ,authenticate
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def home(request):
    if request.user.is_anonymous:
        return redirect("/loginuser")
    return render(request,'home.html')
    #return HttpResponse("this is the homepage")

def helps(request):
    if request.user.is_anonymous:
        return redirect("/loginuser")
    return render(request,'help.html')
    #return HttpResponse("this is the help")

def services(request):
    if request.user.is_anonymous:
        return redirect("/loginuser")
    return render(request,'service.html')
    #return HttpResponse("this is the services")

def about(request):
    if request.user.is_anonymous:
        return redirect("/loginuser")
    return render(request,'about.html')
    #return HttpResponse("this is the about page")

def contacts(request):
    if request.user.is_anonymous:
        return redirect("/loginuser")
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        contact = Contact(name=name, email=email, phone=phone ,date= datetime.today(),message=message)
        contact.save()
        messages.success(request, 'Details recorded! ')
    return render(request,'contact.html')

    #return HttpResponse("this is the contact page")

def index(request):
    if request.user.is_anonymous:
        return redirect("/loginuser")
    return render(request,'index.html')

def loginuser(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        #check if user has enetred correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
            # A backend authenticated the credentials
        else:
            return render(request,'login.html')  
            # No backend authenticated the credentials

    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/loginuser")

def create(request):

    if request.method=="POST":

        username = request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username, email , password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()
        return redirect("/loginuser")
    return render(request,'create.html')
def pay(request):
    if request.user.is_anonymous:
        return redirect("/loginuser")
    return render(request,'pay.html')

def cart(request):
    if request.user.is_anonymous:
        return redirect("/loginuser")
    return render(request,'cart.html')