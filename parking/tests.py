from django.utils import timezone
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from parking.models import Garage, ParkingSpot, Reservation
from rest_framework_simplejwt.tokens import RefreshToken

class ReservationEndTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester2', password='secure123')
        self.garage = Garage.objects.create(name="Testgarage 2", location="Testplatz 2")
        self.spot = ParkingSpot.objects.create(number=88, garage=self.garage, is_reserved=True)

        self.reservation = Reservation.objects.create(
            user_name=self.user.username,
            start_time=timezone.now(),
            spot=self.spot
        )

        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    def test_end_reservation_and_free_spot(self):
        response = self.client.post(f'/api/reservations/{self.reservation.id}/end/')
        self.assertEqual(response.status_code, 200)

        self.spot.refresh_from_db()
        self.assertFalse(self.spot.is_reserved)
