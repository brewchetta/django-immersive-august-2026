from django.urls import path
from . import views

urlpatterns = [
    # READ
    path('', views.home, name="home"),
    path('movies/<int:pk>', views.movie_detail, name="movie_detail"),

    # CREATE
    path('movies/create', views.movie_create, name="movie_create"),

    # EDIT
    path('movies/<int:pk>/edit', views.movie_edit, name="movie_edit"),

    # DELETE
    path('movies/<int:pk>/delete', views.movie_delete, name="movie_delete"),
]

# RESTful ROUTING

# convention - make routes / paths / urls predictable

# READ      GET         /movies         movie_list      show all movies
# READ      GET         /movies/1       movie_detail    show one movie

# CREATE    GET         /movies/create  movie_form      show create movie form
# CREATE    POST        /movies/create  create_movie    create movie from form

# UPDATE    GET         /movies/1       movie_form      show update movie form
# UPDATE    PUT/PATCH   /movies/1       update_movie    update movie from form

# DELETE    DELETE      /movies/1       delete_movie    delete movie