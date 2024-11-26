from ..models import Vehicle
from django.http import JsonResponse
from ..serializers import VehicleSerializer

# test param
def get_available_vehicles():
    mock_data = [
        {"id": 1, "name": "Car A", "brand": "Brand X", "price_per_day": 100.00, "available": True},
        {"id": 2, "name": "Car B", "brand": "Brand Y", "price_per_day": 150.00, "available": True},
        {"id": 3, "name": "Car C", "brand": "Brand Z", "price_per_day": 200.00, "available": False},
    ]
    return JsonResponse(mock_data, safe=False)

# def get_available_vehicles():
#     return Vehicle.objects.filter(available=True)

def create_vehicle(data):
    vehicle = Vehicle.objects.create(**data)
    return vehicle