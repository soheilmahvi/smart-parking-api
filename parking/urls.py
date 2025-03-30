from .views import home, GarageViewSet, ParkingSpotViewSet, ReservationViewSet, RegisterView, end_reservation, MyReservationListView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'garages', GarageViewSet)
router.register(r'spots', ParkingSpotViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('', home),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('garages/', views.GarageListCreateView.as_view()),
    path('parkingspots/', views.ParkingSpotListCreateView.as_view()),
    path('reservations/', views.ReservationListCreateView.as_view()),
    path('reservations/<int:pk>/end/', end_reservation, name='reservation-end'),
    path('my-reservations/', MyReservationListView.as_view(), name='my-reservations'),
]
