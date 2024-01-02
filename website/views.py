from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .form import SignUpForm
from .models import Record
# Create your views here.'
def home(request):
    records = Record.objects.all()
    return render(request,'home.html',{'records':records})
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
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request,'you have been register congetulation!!!!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request,'register.html',{'form':form} )
    return render(request, 'register.html', {'form':form})


def customer_record(request, pk = None):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(pk=pk)
        return render(request, 'record.html',{'customer_record':customer_record})
    else:
        messages.success(request,'You must login to view this page')
        return redirect('login')
    