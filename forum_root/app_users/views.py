from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import AdvUser
from .forms import AuthForm, RegistrationForm

# Create your views here.
class UserRegistrationView(CreateView):
    model = AdvUser
    form_class = RegistrationForm
    template_name = 'register.html'
    succsess_url = reverse_lazy('index')
    
    
class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('index')
    form = AuthForm
    
    
class UserLogoutView(LogoutView):
    next_page = '/'