from django.shortcuts import render
import datetime

#       views always need a `request` param
def home(request):
    return render(request, "game_phone_app/home.html")
    #      render triggers a response

    # template is the HTML your sending

def about(request):
    context = { 
        "most_popular_game": "Flappy Bird",
        "second_popular_game": "Subway Surfer",
        "third_popular_game": "Pokemon Go",
        "current_time": datetime.datetime.now()
    }

    return render(request, "game_phone_app/about.html", context)