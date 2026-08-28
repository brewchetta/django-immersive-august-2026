from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login

def home(request):
    return render(request, 'message_app/home.html')

# AUTH VIEWS

def auth_signup(request):
    if (request.method == "POST"):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # creates a cookie/session which keeps the user logged in
            login(request, user)
            return redirect('home')
        context = { "form": form }
        return render(request, 'message_app/signup.html', context)

    form = SignUpForm()
    context = { "form": form }
    return render(request, 'message_app/signup.html', context)

def auth_login():
    pass

def auth_logout():
    pass