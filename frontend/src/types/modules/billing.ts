export interface Billing {
    billing_id: string;
    booking_id: string;
    amount_due: number;
    payment_status: string;
    payment_method: string;
    payment_date: Date;
}