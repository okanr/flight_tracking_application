import datetime

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Airport, Flight


class AirportTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.from_airport = Airport.objects.create(code='AAA', name='Airport')
        cls.to_airport = Airport.objects.create(code='BBB', name='Airport')
        cls.airport = Airport.objects.create(code='CCC', name='Airport')
        cls.flight = Flight.objects.create(flight_number='TK0000',
                                           take_off=datetime.datetime.now(),
                                           landing=datetime.datetime.now() +
                                                   datetime.timedelta(hours=2),
                                           to_airport=cls.to_airport,
                                           from_airport=cls.from_airport)
        cls.flight2 = Flight.objects.create(flight_number='TK9999',
                                            take_off=datetime.datetime.now(),
                                            landing=datetime.datetime.now() +
                                                    datetime.timedelta(hours=2),
                                            to_airport=cls.to_airport,
                                            from_airport=cls.from_airport)

    def test_read_airport(self):
        """
        Ensure we can get airport objects.
        """
        url = '/api/airport/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_airport(self):
        """
        Ensure we can create airport objects.
        """
        client = APIClient()
        data = {
            'name': 'Airport1',
            'code': 'A11'
        }
        response = client.post('/api/airport/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Airport.objects.count(), 4)

    def test_update_flight(self):
        """
        Ensure we can update airport objects.
        """
        client = APIClient()
        data = {
            'name': 'Airport2',
            'code': 'A22'
        }
        response = client.put(f'/api/airport/{self.from_airport.code}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get(f'/api/airport/{data["code"]}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        name = data['name']
        self.assertEqual(name, 'Airport2')

    def test_delete_flight(self):
        """
        Ensure we can delete airport objects.
        """
        client = APIClient()
        response = client.delete(f'/api/airport/{self.airport.code}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FlightTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.from_airport = Airport.objects.create(code='AAA', name='Airport')
        cls.to_airport = Airport.objects.create(code='BBB', name='Airport')
        cls.flight = Flight.objects.create(flight_number='TK0000',
                                           take_off=datetime.datetime.now(),
                                           landing=datetime.datetime.now() +
                                                   datetime.timedelta(hours=2),
                                           to_airport=cls.to_airport,
                                           from_airport=cls.from_airport)
        cls.flight2 = Flight.objects.create(flight_number='TK9999',
                                            take_off=datetime.datetime.now(),
                                            landing=datetime.datetime.now() +
                                                    datetime.timedelta(hours=2),
                                            to_airport=cls.to_airport,
                                            from_airport=cls.from_airport)

    def test_read_flight(self):
        """
        Ensure we can get flight objects.
        """
        url = '/api/flight/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_flight(self):
        """
        Ensure we can create flight objects.
        """
        client = APIClient()
        data = {
            'flight_number': 'TK1111',
            'take_off': datetime.datetime.now(),
            'landing': datetime.datetime.now() + datetime.timedelta(hours=2),
            'to_airport': self.to_airport.code,
            'from_airport': self.from_airport.code,
        }
        response = client.post('/api/flight/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Flight.objects.count(), 3)

    def test_update_flight(self):
        """
        Ensure we can update flight objects.
        """
        client = APIClient()
        data = {
            'flight_number': 'TK5555',
            'take_off': datetime.datetime.now(),
            'landing': datetime.datetime.now() + datetime.timedelta(hours=2),
            'to_airport': self.to_airport.code,
            'from_airport': self.from_airport.code,
        }
        response = client.put(f'/api/flight/{self.flight.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = client.get(f'/api/flight/{self.flight.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        flight_number = data['flight_number']
        self.assertEqual(flight_number, 'TK5555')

    def test_delete_flight(self):
        """
        Ensure we can delete flight objects.
        """
        client = APIClient()
        response = client.delete(f'/api/flight/{self.flight2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
