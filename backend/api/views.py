from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import VehicleSerializer
from .services.vehicle import get_available_vehicles

class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Car Rental System"})

class VehicleView(APIView):
    def get(self, request):
        return get_available_vehicles()
    #     vehicles = get_available_vehicles()
    #     serializer = VehicleSerializer(vehicles, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     serializer = VehicleSerializer(data=request.data)
    #     if serializer.is_valid():
    #         vehicle = create_vehicle(serializer.validated_data)
    #         return Response(VehicleSerializer(vehicle).data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

