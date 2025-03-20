from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()



#class UserLoginForm(AuthenticationForm):
#    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control',
#                                                             'placeholder': 'Введите имя пользователя'
#                                                             }))
#    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocopmlete': 'current-password',
#                                                                 'class': 'form-control',
#                                                                 'placeholder': 'Введите ваш пароль'
#                                                                 }))
#
    class Meta:
        model = User
        fields = ['username', 'password']
