from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="forum_home"),
    path('create', views.create_post, name="forum_create_post"),
    path('<int:pk>/edit', views.edit_post, name="forum_edit_post"),
]