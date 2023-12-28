from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you have been login!!!!')
            return redirect('home')
        else:
            messages.success(request, 'there was an error please try again...')
            return redirect('login')
    else:
        return render(request, 'login.html')
def logout_user(request):
    logout(request)
    messages.success(request, 'you have been logout!!!!')
    return redirect('login')
def home(request):
    return render(request,'home.html')