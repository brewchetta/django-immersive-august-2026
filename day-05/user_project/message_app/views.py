from django.shortcuts import render
from .forms import SignUpForm

def home(request):
    return render(request, 'message_app/home.html')

# AUTH VIEWS

def signup(request):
    form = SignUpForm()
    context = { "form": form }
    return render(request, 'message_app/signup.html', context)

def login():
    pass

def logout():
    pass