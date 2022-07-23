from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Airport, Flight
from .serializers import AirportSerializer, FlightSerializer


@api_view(['GET'])
def flight_api_overview(request):
    api_urls = {
        'all_items': '/',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)


@api_view(['GET'])
def airport_api_overview(request):
    api_urls = {
        'all_items': '/',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)
