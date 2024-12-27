import { defineStore } from "pinia";
import { Customer } from "@types/modules/customer";

export const useCustomerStore = defineStore('customers', {
    state: () => ({
        customers: [
            {
                customer_id: "1",        
                first_name: "Mohamad Taufik", 
                last_name: "Abd Rahman",       
                email: "mohamadtaufik@taufik.com",
                address: "mohamadtaufik@taufik.com",
                license_type: "0112222222",
                date_of_birth: new Date(),
            },
            {
                customer_id: "2",        
                first_name: "Zarith Sofea", 
                last_name: "Abd Rahman",       
                email: "mohamadtaufik@taufik.com",
                address: "mohamadtaufik@taufik.com",
                license_type: "0112222222",
                date_of_birth: new Date(),
            },
            {
                customer_id: "1",        
                first_name: "Mohamad Shahrul", 
                last_name: "Abd Rahman",       
                email: "mohamadtaufik@taufik.com",
                address: "mohamadtaufik@taufik.com",
                license_type: "0112222222",
                date_of_birth: new Date(),
            },
        ] as Customer[]
    }),
    getters: {
        getCustomers(state): Customer[] {
            return state.customers;
        },
    },
    actions: {
    }
})