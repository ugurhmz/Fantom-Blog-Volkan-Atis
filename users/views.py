from django.shortcuts import render
from django.views.generic import CreateView
from .forms import RegisterForm





class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = '/' # işlem başarılı login page olana kadar, buraya gitsin.