from django.urls import path
from . import views

# all urls are being added to the base url
#                           localhost:8000/about
#                           www.yoursite.com/about

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about_page"),
]

# each url pattern is a route/path/url which activates a specific view

# url and redirect use the name

# {% url 'about_page' %}
# redirect('about_page')