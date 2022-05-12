
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import AdvUser


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class RegistrationForm(UserCreationForm):
    class Meta:
        model = AdvUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'send_messages', 'avatar')