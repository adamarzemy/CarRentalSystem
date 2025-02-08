import { defineStore } from "pinia";

export const useAuthStore = defineStore('auth', {
    state: () => ({
        isAuthenticated: true,
    }),
    getters: {
        getIsAuth(state): boolean {
            return state.isAuthenticated;
        },
    },
    actions: {

    }
})