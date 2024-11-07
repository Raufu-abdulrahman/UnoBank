from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser

from .forms import AccountInfoForm, ProfileInfoForm
from .forms import DepositForm, TransferForm
from .forms import WithdrawalForm
# from .forms import LoginForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    current_user = request.user
    return render(request, 'home.html', {'user':current_user})

def register1(request):
    if request.method == "POST":
        form = AccountInfoForm(request.POST)
        if form.is_valid():
            request.session['account_data'] = form.cleaned_data
            print('Stored!')
            return redirect('register2')
    else:
        form = AccountInfoForm(initial={})
        
    return render(request, 'auth/register.html', {'accountform':form})

def register2(request):
    account_data = request.session.get('account_data')
    
    if not account_data:
        return redirect('register1')
    print('Received')
    
    avatars = [
        'avatars/avatar1.jpg', 
        'avatars/avatar2.jpg', 
        'avatars/avatar3.jpg', 
        'avatars/avatar4.jpg',     
    ]
    
    if request.method == "POST":
        form = ProfileInfoForm(request.POST)
        if form.is_valid():
            print('Gotten')
            user = CustomUser(
                username = account_data['username'], 
                email = account_data['email'],
                pin = account_data['pin'],
            )
            print('Grout!')
            user.set_password(account_data['password'])
            user.phone_number = form.cleaned_data['phone_number']
            user.address = form.cleaned_data['address']
            print('All good here!')
            user.avatar = form.cleaned_data['avatar']
            print('Gotten avatar')
            user.save()
        
            login(request, user)
            return redirect('home')
        
    else:
        form = ProfileInfoForm(initial={})
        
    return render(request, 'auth/register2.html', {'profileform':form, 'avatars':avatars})

def my_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    
    else:
        form = AuthenticationForm(initial={})
        
    return render(request, 'auth/login.html', {'loginform':form})

def banking(request):
    current_user = request.user
    return render(request, 'banking/banking.html', {'user':current_user})

def deposit(request):
    current_user = request.user
    if request.method == "POST":
        form = DepositForm(request.POST)
        if form.is_valid():
            pin = form.cleaned_data.get('pin')
            amount = form.cleaned_data.get('amount')
            if pin == current_user.pin:
                current_user.balance += amount
                current_user.save()
                print(f'Deposit of {amount} successful')
                return redirect('home')
            else:
                print('Incorrect PIN!')
    
    else:
        form = DepositForm(initial={})
        
    return render(request, 'banking/deposit.html', {'user':current_user, 'depositform':form})

def transfer(request):
    current_user = request.user
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            account_number = form.cleaned_data['account_number']
            amount = form.cleaned_data['amount']
            pin = form.cleaned_data['pin']
            
            # Ensure the user has enough balance for the transfer
            if current_user.balance < amount:
                messages.error(request, "Insufficient balance for this transfer.")
                return redirect('transfer')
            
            # Retrieve the recipient user by account number
            recipient = get_object_or_404(CustomUser, account_number=account_number)
            
            # Perform the transfer
            if pin == current_user.pin:
                current_user.balance -= amount  # Deduct from sender
                recipient.balance += amount  # Add to recipient
                
                # Save both users' updated balances
                current_user.save()
                recipient.save()
                
                messages.success(request, f"Successfully transferred ${amount} to account {account_number}.")
                return redirect('home')  # Redirect to an account summary page
            else:
                messages.error(request, 'Incorrect PIN!')
    else:
        form = TransferForm()
    
    return render(request, 'banking/transfer.html', {'transferform': form})

def withdrawal(request):
    current_user = request.user
    if request.method == "POST":
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            pin = form.cleaned_data.get('pin')
            amount = form.cleaned_data.get('amount')
            if pin == current_user.pin:
                current_user.balance -= amount
                current_user.save()
                print(f'Withdrwawl of {amount} successful')
                return redirect('home')
            else:
                print('Incorrect PIN!')
    
    else:
        form = WithdrawalForm(initial={})
        
    return render(request, 'banking/withdraw.html', {'user':current_user, 'withdrawalform':form})