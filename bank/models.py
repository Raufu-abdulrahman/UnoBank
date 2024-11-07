import random

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    
    AVATAR_CHOICES = [
        ('avatars/avatar1.jpg', 'Avatar 1'),
        ('avatars/avatar2.jpg', 'Avatar 2'),
        ('avatars/avatar3.jpg', 'Avatar 3'),
        ('avatars/avatar4.jpg', 'Avatar 4')
    ]
    
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField()
    account_number = models.CharField(
        max_length=8, unique=True, verbose_name=('Account Number'), editable=False 
    )
    phone_number = models.CharField(
        max_length=15, blank=True,
        verbose_name='Phone Number'
    )
    address = models.TextField(blank=True, null=True, verbose_name=("Address"))
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name="Balance")
    pin = models.CharField(max_length=4, default=1234)
    avatar = models.CharField(max_length=100, choices=AVATAR_CHOICES, blank=True, default='avatars/avatar1.jpg')
    
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions_set',
        blank=True,
        help_text='\Specific permissions for this user'
    )
            
    def gen_account_number(self):
        while True:
            account_number = str(random.randint(10000000, 99999999))
            if not CustomUser.objects.filter(account_number=account_number).exists():
                return account_number
            
    def __str__(self):
        return f"{self.username} ({self.account_number})"
    
@receiver(pre_save, sender=CustomUser)
def _post_save_receiver(sender, instance, **kwargs):
    if not instance.account_number:
        instance.account_number = instance.gen_account_number()
        

class Deposit(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, verbose_name="Amount")
    pin = models.CharField(max_length=4)
    
    
class Withdrawal(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, verbose_name="Amount")
    pin = models.CharField(max_length=4)
    
class Transfer(models.Model):
    account_number = models.CharField(max_length=8, verbose_name='Account Number')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Amount')
    pin = models.CharField(max_length=4)
    