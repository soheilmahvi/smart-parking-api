from django.contrib import admin
from .models import Garage, ParkingSpot, Reservation

admin.site.register(Garage)
admin.site.register(ParkingSpot)
admin.site.register(Reservation)
