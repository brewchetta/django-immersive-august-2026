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
        return Response(serializer.data, status=status.HTTP_200_OK)

    # post a new sports car
    if request.method == "POST":
        # load serializer with the request data
        serializer = SportsCarSerializer(data=request.data)
        if serializer.is_valid():
            # save to the db if valid
            serializer.save()
            # send back the new data if created
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # if invalid send back the validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def sports_car_detail():
    pass