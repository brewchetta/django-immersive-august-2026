from django import forms
from .models import Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# refers to the user model/table
User = get_user_model()

# create forms for reviews
# ModelForm aligns itself with columns in your table/model
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']

# create forms for user signup / login
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# inherit from the generic form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())