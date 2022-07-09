import django
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(label="Username", max_length=20)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
