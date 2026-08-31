from django.shortcuts import render, redirect
from .forms import ReviewForm, RegistrationForm

def home(request):
    return render(request, 'review_app/home.html')


def about(request):
    pass


from django.contrib.auth.decorators import login_required

@login_required
def create_review(request):
    if (request.method == "POST"):
        form = ReviewForm(request.POST)
        # attach the current user to the review
        form.instance.user = request.user
        if form.is_valid():
            form.save()
            return redirect('home')
        context = { "form": form }
        return render(request, 'review_app/create_review.html', context)

    context = { "form": ReviewForm() }
    return render(request, 'review_app/create_review.html', context)


from django.contrib.auth import login

def auth_registration(request):
    if (request.method == "POST"):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # form.save will save the new user to the db
            new_user = form.save()
            # login will actually login the new user
            # if a user was already logged in this will overwrite the login
            login(request, new_user)
            return redirect('home')
        context = { "form": form }
        return render(request, 'review_app/auth_registration.html', context)
    
    context = { "form": RegistrationForm() }
    return render(request, 'review_app/auth_registration.html', context)