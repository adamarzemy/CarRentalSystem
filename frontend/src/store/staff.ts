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
        async editStaffProfile(staffProfile :Partial<Staff>){
            try {
                this.staffProfile = { ...this.staffProfile, ...staffProfile };
                return this.staffProfile;
            } catch (error) {
                return error;
            }
        },
    }
})