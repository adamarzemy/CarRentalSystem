export interface Booking {
    booking_id: string;
    customer_id: string;
    vehicle_id: string;
    discount_id: string;
    booking_date: Date;
    pickup_date: Date;
    return_date: Date;
    pickup_location: string;
    return_location: string;
    status: string;
    total_price: number;
    booking_status: string;
    phone_no: string;
    role: string;
    hire_date: Date;
    salary: number;
}