from rest_framework import serializers
from .models import SportsCar

class SportsCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsCar

        # we can add fields individually to decide what to include/exclude
        # fields = ['make', 'model', 'horsepower', 'apple_car_play', 'google_play', 'base_price']

        # or we can add all fields using a shortcut
        fields = '__all__'