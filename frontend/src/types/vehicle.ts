export interface Vehicle {
    vehicle_id: string;
    make: string;
    model: string;
    year: number;
    vehicle_type: string;
    color: string;
    plate_no: string;
    mileage: number;
    current_service_date: Date;
    current_condition: string;
    status: string;
}

export interface VehicleTest {
    brand: string;
    model: string;
    status: string;
}