from django.urls import path
from . import views

urlpatterns = [
    # functional view
    path('', views.home, name="home"),

    # class views:

    # whenever you have a class view you must activate it in the path with .as_view()
    path('about', views.AboutPage.as_view(), name="about"),

    # generic view for a form
    path('gaming/create', views.GamingPCCreateView.as_view(), name="gaming_pc_create"),

    # using the generic form
    path('headphones/create', views.HeadphoneCreateView.as_view(), name="headphone_create"),

    # using ListView
    path('headphones', views.HeadphoneList.as_view(), name="headphone_list"),

    # using DetailView
    path('headphones/<int:pk>', views.HeadphoneDetail.as_view(), name="headphone_detail"),

    # image upload example
    path('memes/create', views.MemesCreate.as_view(), name="memes_create"),

    path('memes', views.MemeList.as_view(), name="meme_list")
]