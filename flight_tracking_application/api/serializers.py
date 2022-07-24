from rest_framework import serializers
from .models import Airport, Flight


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ('code', 'name')


class CountSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return Flight.objects.filter(flight_number=obj['flight_number']).count()

    class Meta:
        model = Flight
        fields = ('flight_number', 'count')


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('flight_number', 'take_off', 'landing', 'to_airport',
                  'from_airport')
