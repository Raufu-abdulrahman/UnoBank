from django import forms
from .models import CustomUser, Deposit, Withdrawal, Transfer

class AccountInfoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'pin']
        labels = {
            'username':'Username*',
            'password':'Passowrd*',
            'email':'Email address*'
        }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'pin':forms.PasswordInput(attrs={'class':'form-control'}),
        }
        
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
        pin = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    def __init__(self, *args, **kwargs):
        super(AccountInfoForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].initial = None
    
        
class ProfileInfoForm(forms.ModelForm):
    
    AVATAR_CHOICES = [
        ('avatars/avatar1.jpg', 'Avatar 1'),
        ('avatars/avatar2.jpg', 'Avatar 2'),
        ('avatars/avatar3.jpg', 'Avatar 3'),
        ('avatars/avatar4.jpg', 'Avatar 4'),
    ]
    
    avatar = forms.ChoiceField(choices=AVATAR_CHOICES, widget=forms.RadioSelect)
    
    class Meta:
        model = CustomUser
        fields = ['phone_number', 'address', 'avatar']
        labels = {
            'phone_number':'Phone Number*',
            'address':'Address*',
            'avatar':'Avatar*'
        }
        widgets = {
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
        }
        

    
class LoginForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class DepositForm(forms.ModelForm):
    
    class Meta:
        model = Deposit
        fields = ['amount', 'pin']
        widgets = {
            'amount':forms.NumberInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
        }


class TransferForm(forms.ModelForm):
    
    class Meta:
        model = Transfer
        fields = ['account_number', 'amount', 'pin']
        widgets = {
            'amount':forms.NumberInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
        }
    
    def clean_account_number(self):
        account_number = self.cleaned_data['account_number']
        if not CustomUser.objects.filter(account_number=account_number).exists():
            raise forms.ValidationError("Recipient with this account number does not exist.")
        return account_number

# class WithdrawalForm(forms.Form):
#     amount = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0.01)
#     pin = forms.NumberInput(),
    
class WithdrawalForm(forms.ModelForm):
    
    class Meta:
        model = Withdrawal
        fields = ['amount', 'pin']
        widgets = {
            'amount':forms.NumberInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
        }
