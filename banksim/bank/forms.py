from django import forms
from .models import Account, Transaction

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['username', 'mobile', 'email', 'occupation', 'password']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_amt', 'user_UPI']

class AccountForm(forms.ModelForm):
    virtual_money = forms.IntegerField(label="Enter Virtual Money (less than 1,000,000)", min_value=0, max_value=1000000)

    class Meta:
        model = Account
        fields = ['username', 'mobile', 'email', 'occupation', 'password']