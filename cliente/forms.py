from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class formCadastro(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='E-mail ja existe')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )