from django.urls import path
from . import views

urlpatterns = [
    #   url   view         name
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("power-of/<int:number_one>/<int:number_two>", views.power_of, name="power_of"),
    path("games/<int:game_id>", views.game_by_id, name="game_by_id"),
]