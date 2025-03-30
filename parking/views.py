from rest_framework import status, viewsets, generics, filters
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse
from django.urls import reverse
from .serializers import RegisterSerializer
from .serializers import GarageSerializer, ParkingSpotSerializer, ReservationSerializer
from .filters import ParkingSpotFilter
from .models import Garage, ParkingSpot, Reservation


class GarageViewSet(viewsets.ModelViewSet):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer

class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        reservation = serializer.save()
        reservation.spot.is_reserved = True
        reservation.spot.save()

    @action(detail=True, methods=['post'])
    def end(self, request, pk=None):
        reservation = self.get_object()
        if reservation.end_time is not None:
            return Response({"detail": "Reservation already ended."}, status=400)
        
        reservation.end_time = timezone.now()
        reservation.save()

        reservation.spot.is_reserved = False
        reservation.spot.save()

        return Response({"detail": "Reservation ended."})
        
        
class GarageListCreateView(generics.ListCreateAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer

class ParkingSpotListCreateView(generics.ListCreateAPIView):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [IsAuthenticated]  # <--- Nur eingeloggte Benutzer!
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ParkingSpotFilter
    ordering_fields = ['id', 'number', 'is_reserved', 'garage']  # Felder, nach denen sortiert werden darf
    
class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
    
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def end_reservation(request, pk):
    try:
        reservation = Reservation.objects.get(pk=pk)
    except Reservation.DoesNotExist:
        return Response({'error': 'Reservierung nicht gefunden.'}, status=404)

    if reservation.end_time:
        return Response({'message': 'Reservierung ist bereits beendet.'})

    reservation.end_time = timezone.now()
    reservation.save()

    spot = reservation.spot
    print("Beende Reservierung:", reservation.id)
    print("Parkplatz vorher:", spot.is_reserved)
    spot.is_reserved = False
    spot.save()
    print("Parkplatz nachher:", spot.is_reserved)

    return Response({'detail': 'Reservation ended.'})

class MyReservationListView(generics.ListAPIView):
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user_name=self.request.user.username)
        
def home(request):
    swagger_url = reverse('schema-swagger-ui')
    return HttpResponse(f"""
        <h2>Welcome to Smart Parking API 🚗</h2>
        <p>Explore the <a href="{swagger_url}">Swagger Documentation</a>.</p>
    """)