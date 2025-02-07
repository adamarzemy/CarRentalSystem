<template>
    <div class="h-screen   bg-gray-800" id="side-bar" :class="dataOpenSideBar == true ? 'side-bar-visible' : 'side-bar-close'">
        <div class="bg-gray-700 h-[50px] flex justify-center items-center ">
            <div class="text-xl font-bold text-center flex items-center justify-center text-white h-full" v-show="dataOpenSideBar">
                APP DEV
            </div>
            <img src="https://avatars.githubusercontent.com/u/97021587?v=4" v-show="!dataOpenSideBar" class="p-1 w-8 h-8 rounded-full ring-2 ring-gray-100 dark:ring-gray-500 " alt="Avatar" />
        </div>
        <div class="flex flex-col justify-between h-[calc(100vh-3rem)] bg-gray-900">
            <div class="menu-man text-left px-2 whitespace-nowrap ">
                <div class="profile flex justify-center items-center text-center p-5 ">
                    <div class="text-center  text-white" v-show="dataOpenSideBar">
                        <img src="https://avatars.githubusercontent.com/u/97021587?v=4" class="p-1 w-24 h-24 rounded-full ring-2 ring-gray-300 dark:ring-gray-500 mb-4" alt="Avatar" />
                        <h5 class="text-xl font-medium leading-tight mb-2"> My Name</h5>
                        <p class="text-gray-500">Admin </p>
                    </div>
                </div>
                <div class="   py-3 rounded-sm cursor-pointer text-gray-300 hover:text-white">
                    <router-link to="/" class="px-2 flex space-x-2">
                        <!-- <span class="pi pi-microsoft" v-tooltip.right="'Dashboard'"></span>  -->
                        <span v-tooltip.right="'Dashboard'" class="pt-1">
                            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
                                <path fill="currentColor" d="M3 13h8V3H3v10zm0 8h8v-6H3v6zm10 0h8V11h-8v10zm0-18v6h8V3h-8z"/>
                            </svg>
                        </span>
                        <span v-show="dataOpenSideBar">Dashboard</span>
                    </router-link>
                </div>
                <div class="   py-3 rounded-md cursor-pointer  text-gray-300 hover:text-white">
                    <router-link to="/vehicles" class="px-2 flex space-x-2">
                        <!-- <span class="pi pi-user " v-tooltip.right="'User'"></span>  -->
                        <span v-tooltip.right="'Vehicles'" class="pt-1">
                            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
                                <path fill="currentColor" d="M18.92 6.01C18.72 5.42 18.16 5 17.5 5h-11c-.66 0-1.21.42-1.42 1.01L3 12v8c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-1h12v1c0 .55.45 1 1 1h1c.55 0 1-.45 1-1v-8l-2.08-5.99zM6.5 16c-.83 0-1.5-.67-1.5-1.5S5.67 13 6.5 13s1.5.67 1.5 1.5S7.33 16 6.5 16zm11 0c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zM5 11l1.5-4.5h11L19 11H5z"/>
                            </svg>
                        </span>
                        <span v-show="dataOpenSideBar">Vehicles</span>
                    </router-link>
                </div>
                <div class="   py-3 rounded-md cursor-pointer  text-gray-300 hover:text-white">
                    <router-link to="/bookings" class="px-2 flex space-x-2">
                        <!-- <span class="pi pi-cart-plus " v-tooltip.right="'Product'"></span>  -->
                        <span v-tooltip.right="'Bookings'" class="pt-1">
                            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
                                <path fill="currentColor" d="M19 3h-1V1h-2v2H8V1H6v2H5c-1.11 0-1.99.9-1.99 2L3 19c0 1.1.89 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V8h14v11zM7 10h5v5H7z"/>
                            </svg>
                        </span>
                        <span v-show="dataOpenSideBar">Bookings</span>
                    </router-link>
                </div>
                <div class="  py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
                    <router-link to="/customers" class="px-2 flex space-x-2">
                        <!-- <span class="pi pi-whatsapp  " v-tooltip.right="'Contact'"></span>  -->
                        <span v-tooltip.right="'Customers'" class="pt-1">
                            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
                                <path fill="currentColor" d="M16 11c1.66 0 2.99-1.34 2.99-3S17.66 5 16 5c-1.66 0-3 1.34-3 3s1.34 3 3 3zm-8 0c1.66 0 2.99-1.34 2.99-3S9.66 5 8 5C6.34 5 5 6.34 5 8s1.34 3 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05 1.16.84 1.97 1.97 1.97 3.45V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"/>
                            </svg>
                        </span>
                        <span v-show="dataOpenSideBar">Customers</span>
                    </router-link>
                </div>
                <div class="  py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
                    <router-link to="/staff" class="px-2 flex space-x-2">
                        <!-- <span class="pi pi-shield " v-tooltip.right="'Customer'"></span>  -->
                        <span v-tooltip.right="'Staff'" class="pt-1">
                            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
                                <path fill="currentColor" d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
                            </svg>
                        </span>
                        <span v-show="dataOpenSideBar">Staff</span>
                    </router-link>
                </div>
                <div class="  py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
                    <router-link to="/maintenance" class="px-2 flex space-x-2">
                        <!-- <span class="pi pi-check-circle " v-tooltip.right="'Activation'"></span>  -->
                        <span v-tooltip.right="'Maintenance'" class="pt-1">
                            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
                                <path fill="currentColor" d="M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.6 4.7C.4 7.1.9 10.1 2.9 12.1c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.3-2.3c.5-.4.5-1.1.1-1.4z"/>
                            </svg>
                        </span>
                        <span v-show="dataOpenSideBar">Maintenance</span>
                    </router-link>
                </div>
                <div class="  py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
                    <router-link to="/billing" class="px-2 flex space-x-2">
                        <!-- <span class="pi pi-slack" v-tooltip.right="'Setting'"></span>  -->
                        <span v-tooltip.right="'Billing'" class="pt-1">
                            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" viewBox="0 0 24 24">
                                <path fill="currentColor" d="M20 4H4c-1.11 0-1.99.89-1.99 2L2 18c0 1.11.89 2 2 2h16c1.11 0 2-.89 2-2V6c0-1.11-.89-2-2-2zm0 14H4v-6h16v6zm0-10H4V6h16v2z"/>
                            </svg>
                        </span>
                        <span v-show="dataOpenSideBar">Billing</span>
                    </router-link>
                </div>
            </div>
            <div class="menu-man text-left px-2 justify-self-end whitespace-nowrap">
                <div class="   py-3 rounded-md cursor-pointer text-gray-300 hover:text-white">
                    <a href="https://website-nuxt-front.vercel.app/" target="_blank" class="px-2 flex space-x-2"><span class="pi pi-question" v-tooltip.right="'About Me'"></span> <span v-show="dataOpenSideBar">About Me</span></a>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script>
export default {
    props: {
        dataOpenSideBar: Boolean
    },
}
</script>
  
<style>
.p-tooltip-text {
    font-size: 10px !important;
}

#side-bar {
    overflow: hidden;
    transition: 300ms;
}

.side-bar-visible {
    width: 250px !important;
}

.side-bar-close {
    width: 50px !important;
}
</style>