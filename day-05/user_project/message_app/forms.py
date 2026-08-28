from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# imports the user model for us using a special, safe function
User = get_user_model()

# signup form is built using a special model form
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
                            # the passwords need to match to create a user