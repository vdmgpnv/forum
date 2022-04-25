from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect, render
from app_users.forms import AuthForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            user_name = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=user_name, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    auth_form.add_error('__all__', 'Ошибка, учетная запись пользователя не активна!')
            else:
                auth_form.add_error('__all__', 'Ошибка, проверьте правильность написания логина и пароля')
    else:
        auth_form = AuthForm()
        context = {
            'form' : auth_form
        }
    return render(request, 'index.html', context=context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form':form})

class AnotherLogoutview(LogoutView):
    #template_name = 'logout.html'
    next_page = '/'    