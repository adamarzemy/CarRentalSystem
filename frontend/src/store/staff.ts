import { defineStore } from "pinia";
import { Staff } from "@types/modules/staff";

export const useStaffProfileStore = defineStore('staffProfile', {
    state: () => ({
        staffProfile: {
            staff_id: "1",        
            first_name: "Mohamad Taufik", 
            last_name: "Abd Rahman",       
            email: "mohamadtaufik@taufik.com",
            phone_no: "0112222222",
            role: "admin",
            hire_date: new Date(),
            salary: 0,
        } as Staff
    }),
    getters: {
        getStaffProfile(state): Staff {
            return state.staffProfile;
        },
    },
    actions: {

    }
})