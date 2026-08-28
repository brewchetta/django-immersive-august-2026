from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    # AUTH ROUTES
    path('signup', views.signup, name="signup"),

    path('login', views.login, name="login"),

    path('logout', views.logout, name="logout")
]

# AUTH PAGES
# sign up/register route
# login route
# logout route