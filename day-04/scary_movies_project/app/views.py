from django.shortcuts import render
from .models import Movie

def home(request):
    # get all movies using Movie
    all_movies = Movie.objects.all()
    # add all_movies to context
    context = { "all_movies": all_movies }
    return render(request, "app/home.html", context)