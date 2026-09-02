from django.urls import path
from . import views

urlpatterns = [
    # functional views
    path('sports_cars', views.sports_car_list),
    path('sports_cars/<int:pk>', views.sports_car_detail),
    # long class views
    path('trading_cards', views.TradingCardList.as_view()),
    # mixing class views
    path('phones', views.PhoneList.as_view()),
    path('phones/<int:pk>', views.PhoneDetail.as_view()),
    # super shortcut class views
    path('channels', views.ChannelList.as_view()),
    path('channels/<int:pk>', views.ChannelDetail.as_view())
]

# RESTFUL ROUTES

#   GET     /sports_cars        return all sportscars
#   POST    /sports_cars        create a new sportscar

#   GET     /sports_cars/:id    return one sportscar
#   PUT     /sports_cars/:id    edit a sportscar
#   DELETE  /sports_cars/:id    delete a sportscar