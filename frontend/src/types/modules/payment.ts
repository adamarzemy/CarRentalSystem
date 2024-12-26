export interface Payment {
    payment_id: string;
    bill_id: string;
    payment_date: Date;
    payment_amount: number;
    payment_status: string;
    payment_method: string;
}