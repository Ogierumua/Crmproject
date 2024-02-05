from django.shortcuts import render, redirect
import mysql.connector
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from .forms import SignupUser


con = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Hailmary@12345.', database = 'crmbase')
cursor = con.cursor()



def index(request):
    
    return render(request, 'index.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been successfully logged in")
            return redirect('signin')
        else:
            messages.warning(request, "you were not sucessfully logged in bad credentials")
            return redirect('signin')
    else:
        return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        form = SignupUser(request.POST)
        if form.is_validate():
            form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password_A']
        user = authenticate(username = username, password = password)
        login(request, user)
        messages.success(request, 'you have successfully registered')
        return redirect('signin')
    else:
        form = SignupUser()
        return render(request, 'signup.html', {'form':form})

def signout(request):
    logout(request)
    messages.success(request, "you have been Logged out successfully")
    return redirect('index')
    
    

def back(request):
    
    return render(request, 'index.html')
    

"""
def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "you have successfully logged in")
            return redirect('index')
        else:
            messages.warning(request, "You were not successfully looged in enter correct credentials")
            return redirect('index')
    else:
        return render(request, 'index.html', {})
    
    
    
    
def logout(request):
    logout(request)
    messages.success(request, "you have successfully logged out")
    return redirect("index")

#def index(request):
    
     #return render(request, 'index.html', {})
    
    
    
"""

# Create your views here.