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


from rest_framework import mixins, generics
from .models import Phone
from .serializers import PhoneSerializer

class PhoneList(
    generics.GenericAPIView,    # GenericAPIView is the basic API view used with mixins
    mixins.ListModelMixin,      # ListModelMixin allows us to see all the models in a get
    mixins.CreateModelMixin     # CreateModelMixin has all the functionality for posting
):
    # queryset is what will be shown in the list
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class PhoneDetail(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,   # to get a single phone
    mixins.UpdateModelMixin,    # update a single phone
    mixins.DestroyModelMixin    # delete a single phone
):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

    # *args are any additional arguments
    # **kargs are additional keyword arguments (such as pk=5)
    def get(self, request, *args, **kargs):
        # we need to make sure we forward the *args and **kargs to the self.method
        return self.retrieve(request, *args, **kargs)

    def put(self, request, *args, **kargs):
        return self.update(request, *args, **kargs)

    def delete(self, request, *args, **kargs):
        return self.destroy(request, *args, **kargs)


from .models import Channel
from .serializers import ChannelSerializer

class ChannelList(generics.ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class ChannelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer