from django.urls import path
from . import views

urlpatterns = [
    #   url   view         name
    path("", views.home, name="home"),
]