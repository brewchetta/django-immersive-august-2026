from django.shortcuts import render

def home(request):
    return render(request, 'message_app/home.html')