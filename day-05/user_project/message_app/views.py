from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate

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


def auth_login(request):
    if (request.method == "POST"):
        form = LoginForm(request.POST)
        if form.is_valid():
            # cleaned_data is the data that's been validated
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # potentially find a user with that username & password
            user = authenticate(request, username=username, password=password)
            if (user):
                # if we do we log them in
                login(request, user)
                return redirect('home')
        # if invalid form or invalid user rerender form & send a message
        context = { "form": form, "message": "Invalid username or password" }
        return render(request, 'message_app/login.html', context)

    form = LoginForm()
    context = { "form": form }
    return render(request, 'message_app/login.html', context)


def auth_logout(request):
    logout(request)
    return redirect('home')