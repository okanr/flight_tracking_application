from rest_framework import serializers
from .models import Airport, Flight


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ('code', 'name')


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('flight_number', 'take_off', 'landing', 'to_airport', 'from_airport')
