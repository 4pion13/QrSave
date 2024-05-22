from django import forms
from django.contrib.auth.forms import UserCreationForm, 
from proApp.models import CustomUser
from django.contrib.auth import get_user_model
    
class CustomUserCreationForm(UserCreationForm):
        class Meta(UserCreationForm):
            model = get_user_model()
            fields = ['first_name', 'username', 'email', 'mobile', 'sponsorId', 'address', 'zipCode', 'country',
                      ' 'user_doc', 'last_name', 'password1', 'password2']
            widgets = {
                'first_name': forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'First Name', 'required': 'required'}),
                'last_name': forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required': 'required'}),
                'username': forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Trading Acc No: (For Login)', 'required': 'required'}),
                'password1': forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Password', 'required': 'required'}),
                'password2': forms.TextInput(
                    attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'required': 'required'}),
                'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile', 'required': 'required'}),
                'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': 'required'}),
                'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
 'user_doc': forms.FileInput(attrs={'class': 'form-control-file',}),
            }