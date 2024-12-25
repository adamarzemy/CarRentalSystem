export interface Discount {
    discount_id: string;
    discount_code: string;
    discount_percentage: number;
    valid_from: Date;
    valid_to: Date;
    description: string;
}