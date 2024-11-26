from django.urls import path
from .views import HelloWorldView, VehicleView
from . import views

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('vehicles/', VehicleView.as_view(), name='vehicle-list'),
]
