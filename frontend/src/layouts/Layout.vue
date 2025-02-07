<script setup lang="ts">
import ArrowLeftPipeIcon from '@icons/ArrowLeftPipeIcon.vue';
import { onMounted } from 'vue';

defineProps({
    layoutType: String,
});

onMounted(() => {
    if (typeof document !== 'undefined') {
        const textElement = document.querySelector('.animated-text');
        if (textElement) {
            textElement.classList.add('fade-in');
        }
    }
});
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
                <h1 class="animated-text font-bold text-4xl">
                    <span class="welcome-text">Welcome to</span>
                    <span class="car-rental-text text-blue-600">Car Rental</span>
                    <span class="system-text">System</span>
                </h1>
                <router-link 
                    to="/booking" 
                    class="booking-button flex gap-2 justify-center rounded-full mt-8"
                    tag="button"
                >
                    <span>Book Now!</span>
                    <ArrowLeftPipeIcon class="mt-1"/>
                </router-link>
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
    color: white;
    text-decoration: none;
    background: transparent;
    border-radius: 8px;
    transition: background-color 0.3s, color 0.3s;
}

.nav-link:hover {
    background-color: #14b8a6;
    color: white;
}

/* Animation styles */
.animated-text {
    opacity: 0;
    transform: translateY(20px);
}

.animated-text span {
    display: inline-block;
    opacity: 0;
    transform: translateY(20px);
}

.welcome-text {
    animation: fadeInUp 0.8s ease forwards 0.5s;
}

.car-rental-text {
    animation: fadeInUp 0.8s ease forwards 1s;
}

.system-text {
    animation: fadeInUp 0.8s ease forwards 1.5s;
}

.booking-button {
    opacity: 0;
    animation: fadeInUp 0.8s ease forwards 2s;
    padding: 12px 24px;
    background-color: #14b8a6;
    color: white;
    transition: transform 0.3s, background-color 0.3s;
}

.booking-button:hover {
    transform: translateY(-2px);
    background-color: #0d9488;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
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

    .animated-text {
        font-size: 1.8rem;
    }
}
</style>
