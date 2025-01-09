# Generated by Django 5.1.4 on 2025-01-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('bill_id', models.IntegerField(primary_key=True, serialize=False)),
                ('booking_id', models.IntegerField()),
                ('amount_due', models.FloatField()),
                ('payment_status', models.IntegerField()),
                ('payment_method', models.IntegerField()),
                ('payment_date', models.DateField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('created_by', models.CharField(max_length=500)),
                ('updated_by', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('vehicle_id', models.IntegerField()),
                ('discount_id', models.CharField(max_length=25)),
                ('booking_date', models.DateField()),
                ('pickup_date', models.DateField()),
                ('return_date', models.DateField()),
                ('pickup_location', models.CharField(max_length=500)),
                ('return_location', models.CharField(max_length=500)),
                ('status', models.IntegerField()),
                ('total_price', models.FloatField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('created_by', models.CharField(max_length=500)),
                ('updated_by', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=500)),
                ('license_type', models.CharField(max_length=25)),
                ('date_of_birth', models.DateField()),
                ('register_date', models.DateField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('created_by', models.CharField(max_length=500)),
                ('updated_by', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('discount_id', models.IntegerField(primary_key=True, serialize=False)),
                ('discount_code', models.CharField(max_length=25)),
                ('discount_percentage', models.IntegerField()),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField()),
                ('discount_description', models.CharField(max_length=50)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('created_by', models.CharField(max_length=500)),
                ('updated_by', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('bill_id', models.IntegerField()),
                ('payment_date', models.DateField()),
                ('payment_amount', models.FloatField()),
                ('payment_status', models.IntegerField()),
                ('payment_method', models.IntegerField()),
                ('create_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('created_by', models.CharField(max_length=500)),
                ('updated_by', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=500)),
                ('last_name', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('phone_number', models.IntegerField()),
                ('job_role', models.IntegerField()),
                ('hire_date', models.DateField()),
                ('salary', models.FloatField()),
                ('employee_password', models.CharField(max_length=50)),
                ('created_date', models.DateField()),
                ('updated_at', models.DateField()),
                ('created_by', models.CharField(max_length=500)),
                ('updated_by', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.IntegerField(primary_key=True, serialize=False)),
                ('make', models.CharField(max_length=50)),
                ('vehicle_model', models.CharField(max_length=50)),
                ('model_year', models.IntegerField()),
                ('vehicle_type', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('plate_number', models.CharField(max_length=25)),
                ('mileage', models.IntegerField()),
                ('current_service_date', models.DateField()),
                ('current_location', models.CharField(max_length=50)),
                ('status', models.IntegerField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('created_by', models.CharField(max_length=500)),
                ('updated_by', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleMaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_id', models.IntegerField()),
                ('maintenance_date', models.DateField()),
                ('service_description', models.CharField(max_length=500)),
                ('mileage_at_service', models.IntegerField()),
                ('service_cost', models.FloatField()),
                ('next_service_mileage', models.IntegerField()),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField()),
                ('created_by', models.CharField(max_length=500)),
                ('updated_by', models.CharField(max_length=500)),
            ],
        ),
    ]