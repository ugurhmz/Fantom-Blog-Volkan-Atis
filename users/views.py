from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import RegisterForm





class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = '/' # işlem başarılı login page olana kadar, buraya gitsin.


class UserLogin(LoginView):
    template_name='users/login.html'


class UserLogout(LogoutView):
    template_name = 'users/logout.html'