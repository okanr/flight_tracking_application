from django.db.models import Count
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Airport, Flight
from .serializers import AirportSerializer, FlightSerializer, CountSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Airports': '/airport',
        'Flights': '/flight',
    }

    return Response(api_urls)


class AirportViewSet(viewsets.ModelViewSet):
    serializer_class = AirportSerializer
    queryset = Airport.objects.all()


class FlightViewSet(viewsets.ModelViewSet):
    serializer_class = FlightSerializer
    queryset = Flight.objects.all()

    @action(detail=False, methods=['GET'], name='Flight Counts Based On Flight Number')
    def highlight(self, request, *args, **kwargs):
        queryset = Flight.objects.all().values('flight_number').\
            annotate(count=Count('flight_number'))

        serializer = CountSerializer(queryset, many=True)
        return Response(serializer.data)
