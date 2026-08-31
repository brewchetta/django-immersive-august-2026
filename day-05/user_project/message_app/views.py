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


# MESSAGE VIEWS

from .forms import MessageForm
from django.contrib.auth.decorators import login_required

# @login_required forces the route to be blocked if someone isn't logged in
@login_required
def message_create(request):
    if (request.method == "POST"):
        form = MessageForm(request.POST)
        # attach the user to the form as the sender
        form.instance.sender = request.user
        if form.is_valid():
            form.save()
            return redirect('home')
        context = { "form": form }
        return render(request, 'message_app/message_create.html', context)

    form = MessageForm()
    context = { "form": form }
    return render(request, 'message_app/message_create.html', context)


from django.shortcuts import get_object_or_404
from .models import Message
from django.http import Http404

# helper to make sure user is the same as the message sender
def match_user_or_404(request, message):
    if (request.user != message.sender):
            # go to 404 page if user != sender
            raise Http404

# must be logged in to even see this page
@login_required
def message_delete(request, pk):
    # get message as usual
    message = get_object_or_404(Message, pk=pk)

    # use helper to check this is a valid user/sender
    match_user_or_404(request, message)

    # normal delete stuff
    if (request.method == "POST"):
        message.delete()
        return redirect('home')

    # normal show confirmation page stuff
    context = { "message": message }
    return render(request, 'message_app/message_delete.html', context)