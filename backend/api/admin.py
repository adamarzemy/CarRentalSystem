from django.contrib import admin
from .models import Customer, VehicleMaintenance, Staff, Booking, Vehicle, Billing, Discount, Payment

# Registering the Customer model
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'license_type', 'date_of_birth', 'register_date', 'create_by')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')

# Registering the VehicleMaintenance model
@admin.register(VehicleMaintenance)
class VehicleMaintenanceAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id', 'maintenance_date', 'service_description', 'mileage_at_service', 'service_cost', 'next_service_mileage', 'created_by')
    search_fields = ('vehicle_id', 'service_description')

# Registering the Staff model
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'first_name', 'last_name', 'email', 'phone_number', 'job_role', 'hire_date', 'salary')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')

# Registering the Booking model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'customer', 'vehicle', 'discount_id', 'booking_date', 'pickup_date', 'return_date', 'pickup_location', 'return_location', 'status', 'total_price')
    search_fields = ('customer__first_name', 'customer__last_name', 'vehicle__plate_number')

# Registering the Vehicle model
@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id', 'make', 'vehicle_model', 'model_year', 'vehicle_type', 'color', 'plate_number', 'mileage', 'current_service_date', 'current_location')
    search_fields = ('plate_number', 'make', 'vehicle_model')

# Registering the Billing model
@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('bill_id', 'booking', 'amount_due', 'payment_status', 'payment_method', 'payment_date')
    search_fields = ('booking__booking_id', 'payment_status')

# Registering the Discount model
@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('discount_id', 'discount_code', 'discount_percentage', 'valid_from', 'valid_to', 'discount_description')
    search_fields = ('discount_code', 'discount_description')

# Registering the Payment model
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'bill', 'payment_date', 'payment_amount', 'payment_status', 'payment_method')
    search_fields = ('bill__bill_id',)

