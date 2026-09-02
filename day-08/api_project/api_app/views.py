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


@api_view( [ "GET", "PUT", "PATCH", "DELETE" ] )
def sports_car_detail(request, pk):
    # try to find sports car in db
    try:
        sports_car = SportsCar.objects.get(pk=pk)
    # if does not exist send a 404
    except SportsCar.DoesNotExist:
        return Response({"error": "404 NOT FOUND"}, status=status.HTTP_404_NOT_FOUND)

    # GET THE SPORTS CAR
    if (request.method == "GET"):
        # load sports car into serializer
        serializer = SportsCarSerializer(sports_car)
        # send serialized data
        return Response(serializer.data, status=status.HTTP_200_OK)

    # UPDATE THE SPORTS CAR
    if (request.method == "PUT" or request.method == "PATCH"):
        # serializer with the car and edit data
        serializer = SportsCarSerializer(sports_car, data=request.data, partial=True)
                        # partial=True means we aren't trying to edit the full object
        if serializer.is_valid():
            # if valid save and return
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        # if invalid send errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE THE SPORTS CAR
    if (request.method == "DELETE"):
        # delete the car
        sports_car.delete()
        # return an empty response
        return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.views import APIView
from .models import TradingCard
from .serializers import TradingCardSerializer

class TradingCardList(APIView):

    def get(self, request, format=None):
        trading_cards = TradingCard.objects.all()
        serializer = TradingCardSerializer(trading_cards, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TradingCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)