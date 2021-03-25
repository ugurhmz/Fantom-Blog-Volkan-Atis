from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField(max_length = 80)
    password1 = forms.CharField()
    password2 = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2')
