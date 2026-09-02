from django.urls import path
from . import views

urlpatterns = [
    path('sports_cars', views.sports_car_list),
    path('sports_cars/<int:pk>', views.sports_car_detail)
]

# RESTFUL ROUTES

#   GET     /sports_cars        return all sportscars
#   POST    /sports_cars        create a new sportscar

#   GET     /sports_cars/:id    return one sportscar
#   PUT     /sports_cars/:id    edit a sportscar
#   DELETE  /sports_cars/:id    delete a sportscar