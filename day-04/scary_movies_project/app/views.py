from django.shortcuts import render, get_object_or_404, redirect

from .models import Movie

from .forms import MovieForm

# READ #

def home(request):
    # WITH QUERY PARAMS ##########
    # see if title is in the query params
    # http://127.0.0.1:8000/?title=Alien    <<< Alien is the title
    title = request.GET.get('title')
    # if we have a title we find and show the movie
    if (title):
        movie = get_object_or_404( Movie, title__iexact=title )
        # title__iexact means we are looking for a match but ignore uppercase or lowercase
        context = { "movie": movie }
        return render(request, "app/movie_detail.html", context)

    # if no title: do the normal flow

    # NORMAL FLOW ################

    # get all movies using Movie
    all_movies = Movie.objects.all()
    # add all_movies to context
    context = { "all_movies": all_movies }
    return render(request, "app/home.html", context)

def movie_detail(request, pk):
    # movie = Movie.objects.get(pk=pk)
    movie = get_object_or_404( Movie, pk=pk )
    # if we don't find the movie we throw 404 page

    context = { "movie": movie }
    return render(request, 'app/movie_detail.html', context)

# CREATE #

def movie_create(request):
    # someone has gone to the page and wants to see the form
    if request.method == "GET":
        context = { "form": MovieForm() }
        return render(request, 'app/movie_create.html', context)

    # submitted the form so let's process the form inputs
    if request.method == "POST":
        # request.POST is the body of material that got submitted
        form = MovieForm(request.POST)
        # check that the data is good
        if form.is_valid():
            # cleaned_data is the validated data in the form
            title = form.cleaned_data['title']
            poster_url = form.cleaned_data['poster_url']
            # create a new movie instance with the inputs
            new_movie = Movie(title=title, poster_url=poster_url)
            # save to db
            new_movie.save()
            # send to home page
            return redirect('home')