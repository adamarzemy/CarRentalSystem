from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class HomeView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the Car Rental System!"}, status=200)


class CustomerView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VehicleView(APIView):
    def get(self, request):
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookingView(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VehicleMaintenanceView(APIView):
    def get(self, request):
        maintenances = VehicleMaintenance.objects.all()
        serializer = VehicleMaintenanceSerializer(maintenances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class StaffView(APIView):
    def get(self, request):
        staff_members = Staff.objects.all()
        serializer = StaffSerializer(staff_members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BillingView(APIView):
    def get(self, request):
        billings = Billing.objects.all()
        serializer = BillingSerializer(billings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DiscountView(APIView):
    def get(self, request):
        discounts = Discount.objects.all()
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PaymentView(APIView):
    def get(self, request):
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
