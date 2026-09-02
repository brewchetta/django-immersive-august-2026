from .models import SportsCar
from .serializers import SportsCarSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# api view limits this to only GET and POST requests
@api_view( [ "GET", "POST" ] )
def sports_car_list(request):

    # get all sports cars
    if request.method == "GET":
        sports_cars = SportsCar.objects.all()
        # serialize data into dictionary/json form, many=True means serialize all cars
        serializer = SportsCarSerializer(sports_cars, many=True)
        # send the cars back to the user who made the request
        return Response(serializer.data)

    # post a new sports car
    if request.method == "POST":
        pass


def sports_car_detail():
    pass