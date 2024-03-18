from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login, logout as auth_logout
# Create your views here.
def index(request):
    # userdetails=[
    #     {"name":"Sujitha", "age":23},
    #     {"name":"Harry", "age":13},
    #     {"name":"Potter", "age":20}
    # ]
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if not (username and email and password):
            return render(request,"signup.html",{'error':'All fields are required'})
        if User.objects.filter(username = username).exists():
            return render(request,"signup.html",{'error':'Username already exists'})
        saving = User.objects.create_user(username = username, email = email, password = password)
        auth_login(request,saving)
        return redirect('index')
    return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('index')
        else:
            return render(request,'login.html',{'error':'Invalid credentials'})
    return render(request,'login.html')