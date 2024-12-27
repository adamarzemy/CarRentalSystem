import { defineStore } from "pinia";
import { Vehicle } from "@types/modules/vehicle";

export const useVehicleStore = defineStore('vehicle', {
    state: () => ({
        vehicles: [
            {
                brand: 'Toyota',
                model: 'Vios',
                status: 'New',
            },
            {
                brand: 'Honda',
                model: 'Accord',
                status: 'New',
            },
            {
                brand: 'Honda',
                model: 'City',
                status: 'Used',
            }
        ] as Vehicle[], 
    }),
    getters: {
        getVehicles(state): Vehicle[] {
            return state.vehicles;
        },
    },
    actions: {

    }
})