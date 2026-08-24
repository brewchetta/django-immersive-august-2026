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

def power_of(request, number_one, number_two):
    result = number_one ** number_two
    context = {
        "result": result,
        "number_one": number_one,
        "number_two": number_two,
    }
    return render(request, "game_phone_app/power_of.html", context)

all_games = [
    { "name": "Chess", "download_size": "2MB", "id": 0 },
    { "name": "Roblox", "download_size": "2GB", "id": 1 },
    { "name": "Candy Crush", "download_size": "6MB", "id": 2 }
]

def game_by_id(request, game_id):
    try:
        game = all_games[game_id]

        context = {
            "game": game
        }

        return render(request, "game_phone_app/game_by_id.html", context)

    except IndexError:
        return render(request, "game_phone_app/404.html")

def games(request):
    context = {
        "games": all_games
    }
    return render(request, "game_phone_app/games.html", context)