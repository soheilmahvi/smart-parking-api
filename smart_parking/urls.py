from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from parking.views import home

schema_view = get_schema_view(
   openapi.Info(
      title="Smart Parking API",
      default_version='v1',
      description="Dokumentation für dein Parking System",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mahvisoheyl@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('parking.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', home),
]
