from django import forms
from .models import CustomUser

class AccountInfoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        labels = {
            'username':'Username*',
            'password':'Passowrd*',
            'email':'Email address*'
        }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }
        
        password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
        
        
    # def __init__(self, *args, **kwargs):
    #     super(AccountInfoForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].inital = ''
    #     self.fields['email'].inital = ''
    #     self.fields['password'].inital = ''
        
        
class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone_number', 'address', 'avatar']
        labels = {
            'phone_number':'Phone Number*',
            'address':'Address*',
        }
        widgets = {
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control'}),
            'avatar':forms.Select(attrs={'class':'form-control'})
        }
        
    # def __init__(self, *args, **kwargs):
    #     super(ProfileInfoForm, self).__init__(*args, **kwargs)
    #     self.fields['phone_number'].inital = ''
    #     self.fields['address'].inital = ''
    
class LoginForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password']
