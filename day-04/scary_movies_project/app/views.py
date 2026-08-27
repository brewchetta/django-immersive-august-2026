from django.shortcuts import render, get_object_or_404
from .models import Movie

def home(request):
    # get all movies using Movie
    all_movies = Movie.objects.all()
    # add all_movies to context
    context = { "all_movies": all_movies }
    return render(request, "app/home.html", context)

def movie_detail(request, pk):
    # movie = Movie.objects.get(pk=pk)
    movie = get_object_or_404( Movie, pk=pk )

    context = { "movie": movie }
    return render(request, 'app/movie_detail.html', context)