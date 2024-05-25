from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import InformationAboutBoxes
    
class InfoBoxes(forms.ModelForm):
    class Meta:
        model = InformationAboutBoxes
        fields = ['title', 'content', 'img']