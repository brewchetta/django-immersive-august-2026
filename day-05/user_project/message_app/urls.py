from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    # AUTH ROUTES
    path('signup', views.auth_signup, name="auth_signup"),

    path('login', views.auth_login, name="auth_login"),

    path('logout', views.auth_logout, name="auth_logout")
]

# AUTH PAGES
# sign up/register route
# login route
# logout route