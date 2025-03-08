from django.db import models
class Account(models.Model):
    idno = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    mobile = models.BigIntegerField()
    email = models.EmailField(unique=True)
    occupation = models.CharField(max_length=255)
    dor = models.DateField(auto_now_add=True)
    balance = models.IntegerField(default=0)
    bank_pin = models.IntegerField(default=0000)
    password = models.CharField(max_length=255)
    upi = models.CharField(max_length=255, unique=True)
      # Add this field

    def __str__(self):
        return self.username

class Transaction(models.Model):
    users_name = models.CharField(max_length=255)
    transaction_id = models.IntegerField(primary_key=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    transaction_amt = models.IntegerField()
    credit_or_debit = models.CharField(max_length=30)
    user_UPI = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.users_name} - {self.transaction_id}"
# Create your models here.
