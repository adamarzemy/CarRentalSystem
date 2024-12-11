<script setup lang="ts">
import ArrowLeftPipeIcon from '@icons/ArrowLeftPipeIcon.vue';

defineProps({
    layoutType: String,
})
</script>

<template>
    <div class="parent-overlay">
        <div class="overlay"></div>
        <div class="content">
            <nav class="flex flex-col sm:flex-row justify-end items-center space-y-2 sm:space-y-0 sm:space-x-5 gap-2">
                <ul class="flex flex-col sm:flex-row items-center space-y-2 sm:space-y-0 sm:space-x-5">
                    <li>
                        <router-link to="/" class="nav-link">
                            Home
                        </router-link>
                    </li>
                    <li>
                        <router-link to="/login" class="nav-link">
                            Login
                        </router-link>
                    </li>
                </ul>
            </nav>
            <div v-if="layoutType == 'homePage'" class="home-container mt-80 text-white">
                <h1 class="font-bold text-4xl">Hello , Welcome to <span class="text-blue-600">Car Rental</span> System</h1>
                <router-link 
                    to="/booking" 
                    class="flex gap-2 justify-center rounded-full"
                    tag="button"
                >
                    <span>Booking Now ! </span>
                    <ArrowLeftPipeIcon class="mt-1"/>
                </router-link>
            </div>
            <div v-else-if="layoutType == 'bookingPage'" class="home-container mt-80 text-white">
                
            </div>
            <div v-else-if="layoutType == 'loginPage'" class="home-container mt-80 text-white">
                <h1 class="font-bold text-4xl"><span class="text-blue-600">Login</span> Page</h1>
            </div>
        </div>
    </div>
</template>

<style>
.parent-overlay {
    position: relative;
    width: 100%;
    height: 100vh;
    background: url('@images/car-rental-bg-beach.jpg') no-repeat center center/cover;
    overflow: hidden;
}

.overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.65);
    z-index: 1;
}

.content {
    position: relative;
    z-index: 2;
    color: white;
    text-align: center;
    padding: 20px;
}

.nav-link {
    font-weight: 600;
    padding: 10px 20px;
    color: black;
    text-decoration: none;
    background: transparent;
    border-radius: 8px;
    transition: background-color 0.3s, color 0.3s;
}

.nav-link:hover {
    background-color: #14b8a6;
    color: white;
}

@media (max-width: 640px) {
    .parent-overlay {
        height: 100vh; 
    }

    .content {
        padding: 10px;
    }

    .nav-link {
        font-size: 14px;
    }
}
</style>
