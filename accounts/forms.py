from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

user = get_user_model()

class SignInForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your username",
        })
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your password",
        })
    )


class SignUpForm(UserCreationForm):

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder" : "Enter a password",
        })
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
                "placeholder" : "Enter password again",
                "autocomplete": "new-password",
        })
    )

    class Meta:
        model = user
        fields = ['username', 'email', 'password1', 'password2']

        widgets = {
            "username" : forms.TextInput(attrs={
                "placeholder" : "Enter a username",
            }),
            "email" : forms.EmailInput(attrs={
                "placeholder" : "Enter your e-mail address",
            }),
        }