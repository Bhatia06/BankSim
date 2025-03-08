from django.shortcuts import render, redirect
from .models import Account, Transaction
from .forms import AccountForm, TransactionForm
import random as rn
from datetime import datetime

def home(request):
    return render(request, 'bank/home.html')

def create_account(request):
    if request.method == 'POST':
        templist = list()
        form = AccountForm(request.POST)
        if form.is_valid():
            temp = rn.randint(1000,9999)
            account = form.save(commit=False)
            account.idno = rn.randint(1000, 999999)
            account.upi = account.email.split('@')[0] + '@oktestbank'
            account.balance = form.cleaned_data['virtual_money']
            account.bank_pin = temp
            account.save()
            return render(request, 'bank/account_created.html', {
                'user_id': account.idno,
                'bank_pin': temp,  # Generate a random bank pin
            })
    else:
        form = AccountForm()
    return render(request, 'bank/create_account.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            account = Account.objects.get(email=email, password=password)
            request.session['user_id'] = account.idno
            return redirect('dashboard')
        except Account.DoesNotExist:
            return render(request, 'bank/login.html', {'error': 'Invalid credentials'})
    return render(request, 'bank/login.html')

def dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    account = Account.objects.get(idno=user_id)
    return render(request, 'bank/dashboard.html', {'account': account})

def credit(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.users_name = Account.objects.get(idno=user_id).username
            transaction.transaction_id = rn.randint(10000, 999999)
            transaction.save()
            return redirect('dashboard')
    else:
        form = TransactionForm()
    return render(request, 'bank/credit.html', {'form': form})

def logout(request):
    request.session.flush()
    return redirect('home')

def show_balance(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    account = Account.objects.get(idno=user_id)
    return render(request, 'bank/show_balance.html', {'account': account})

def view_transactions(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    account = Account.objects.get(idno=user_id)
    transactions = Transaction.objects.filter(users_name=account.username)
    return render(request, 'bank/view_transactions.html', {'transactions': transactions})

#loan ka option.