from django.db import models
from django.utils import timezone

class Garage(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    # ✅ Neue Spalte hinzufügen
    level = models.CharField(max_length=50, default='EG')  # EG = Erdgeschoss
    def __str__(self):
        return self.name

class ParkingSpot(models.Model):
    garage = models.ForeignKey(Garage, on_delete=models.CASCADE, related_name='spots')
    number = models.IntegerField()
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f"Spot {self.number} in {self.garage.name}"

class Reservation(models.Model):
    user_name = models.CharField(max_length=100)
    spot = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)  # NEU: Für Beenden

    def __str__(self):
        return f"{self.user_name} reserved {self.spot}"
