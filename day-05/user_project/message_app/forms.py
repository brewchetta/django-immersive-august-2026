from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

# imports the user model for us using a special, safe function
User = get_user_model()

# signup form is built using a special model form
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
                            # the passwords need to match to create a user

# a generic form for the login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    # transform into password input
    password = forms.CharField(widget=forms.PasswordInput)