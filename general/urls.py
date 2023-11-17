from django.urls import path
from .views import CityAPIView, VehicleAPIView

urlpatterns = [
    path('locations/', CityAPIView.as_view()),
    path('vehicles/', VehicleAPIView.as_view())
]