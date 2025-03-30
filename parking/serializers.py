from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import generics
from .models import Garage, ParkingSpot, Reservation

class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = ['id', 'name', 'location', 'level']

class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        spot = data['spot']
        if spot.is_reserved:
            raise serializers.ValidationError("Dieser Parkplatz ist bereits reserviert.")
        return data

    def create(self, validated_data):
        # Beim Reservieren setzen wir is_reserved = True
        spot = validated_data['spot']
        spot.is_reserved = True
        spot.save()
        return super().create(validated_data)

class ParkingSpotListCreateView(generics.ListCreateAPIView):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user