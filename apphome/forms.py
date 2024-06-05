from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

    
class NameInfo(forms.Form):
    first_name = forms.CharField(label="Ваше имя", max_length=100, widget= forms.TextInput(attrs={'class':'form-control',"type":"text",'onkeypress':'noDigits(event)'}))
    last_name = forms.CharField(label="Ваша фамилия", max_length=100, widget= forms.TextInput(attrs={'class':'form-control',"type":"text",'onkeypress':'noDigits(event)'}))





