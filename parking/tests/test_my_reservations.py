from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from parking.models import ParkingSpot, Reservation
from datetime import datetime

class MyReservationsTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Zwei User anlegen
        self.user1 = User.objects.create_user(username='alice', password='alicepass')
        self.user2 = User.objects.create_user(username='bob', password='bobpass')

        # Zwei Parkplätze
        self.spot1 = ParkingSpot.objects.create(number=1, is_reserved=False, garage_id=1)
        self.spot2 = ParkingSpot.objects.create(number=2, is_reserved=False, garage_id=1)

        # Reservierungen
        Reservation.objects.create(user_name='alice', spot=self.spot1, start_time=datetime.now())
        Reservation.objects.create(user_name='bob', spot=self.spot2, start_time=datetime.now())

    def test_user_only_sees_own_reservations(self):
        # Login als alice
        self.client.login(username='alice', password='alicepass')

        response = self.client.get('/api/my-reservations/')
        self.assertEqual(response.status_code, 200)

        reservations = response.json()
        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0]['user_name'], 'alice')
