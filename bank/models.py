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
        ('avatar1.png', 'Avatar 1'),
        ('avatar2.png', 'Avatar 2'),
        ('avatar3.png', 'Avatar 3'),
        ('avatar4.png', 'Avatar 4')
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
    avatar = models.CharField(
        max_length=50, choices = AVATAR_CHOICES, default='avatar1.png', verbose_name='Avatar'
    )
    
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
        
    