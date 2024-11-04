from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser

from .forms import AccountInfoForm, ProfileInfoForm
# from .forms import LoginForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def register1(request):
    if request.method == "POST":
        form = AccountInfoForm(request.POST)
        if form.is_valid():
            request.session['account_data'] = form.cleaned_data
            print('Stored!')
            return redirect('register2')
    else:
        form = AccountInfoForm()
        
    return render(request, 'auth/register.html', {'accountform':form})

def register2(request):
    account_data = request.session.get('account_data')
    
    if not account_data:
        return redirect('register1')
    
    if request.method == "POST":
        form = ProfileInfoForm(request.POST, request.FILES)
        if form.is_valid():
            print('Go On!')
            user = CustomUser(
                username = account_data['username'], 
                email = account_data['email'],
            )
            print('User accepted')
            user.set_password(account_data['password'])
            user.phone_nummber = form.cleaned_data['phone_number']
            user.address = form.cleaned_data['address']
            user.avatar = form.cleaned_data['avatar']
            user.save()
            print('USER SAVED')
            
            login(request, user)
            return redirect('home')
        
    else:
        form = ProfileInfoForm()
        
    return render(request, 'auth/register2.html', {'profileform':form})

def my_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        print('form ye!')
        if form.is_valid():
            print('somethng')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print('authenticating!!!')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    
    else:
        form = AuthenticationForm()
        
    return render(request, 'auth/login.html', {'loginform':form})