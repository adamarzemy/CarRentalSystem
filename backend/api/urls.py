from django.urls import path, include
from django.contrib import admin
from .views import HelloWorldView, VehicleView
from . import views

urlpatterns = [
    path('', HelloWorldView.as_view(), name='home'),  # Add this line for the root path
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('vehicles/', VehicleView.as_view(), name='vehicle-list'),
    path('customer/', VehicleView.as_view(), name='customer-list'),
    path('vehiclesmaintenance/', VehicleView.as_view(), name='vehiclemaintenance-list'),
    path('staff/', VehicleView.as_view(), name='staff-list'),
    path('booking/', VehicleView.as_view(), name='booking-list'),
    path('billing/', VehicleView.as_view(), name='biling-list'),
    path('discount/', VehicleView.as_view(), name='discount-list'),
    path('payment/', VehicleView.as_view(), name='payment-list')
]

