from django.shortcuts import render

def home(request):
    return render(request, 'review_app/home.html')

def about(request):
    pass

def create_review(request):
    pass

def auth_registration(request):
    pass