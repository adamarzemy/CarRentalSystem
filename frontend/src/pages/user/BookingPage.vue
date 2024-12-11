<script setup lang="ts">
import { ref } from 'vue';
import Layout from '@layouts/Layout.vue'; 
import Card from '@components/Card.vue'; 
import TextInput from '@components/TextInput.vue';
import DropDown from '@components/DropDown.vue';

const layoutType: string = 'bookingPage';
const inputValue = ref('');

// const hasAlert = ref<boolean>(true)
const alertMessage = ref<string>('');
const alertType = ref<'success' | 'error' | null>(null);

const showAlert = (message: string, type: 'success' | 'error') => {
  alertMessage.value = message;
  alertType.value = type;
  console.log(alertMessage)
};

const closeAlert = () => {
  alertMessage.value = '';
  alertType.value = null;
};

</script>

<template>
  <!-- <Layout :layoutType="layoutType"> -->
    <div class="parent-overlay">
        <div class="overlay"></div>
        <div class="content">
            <Alert v-if="alertMessage" :message="alertMessage" :type="alertType" @close="closeAlert" />
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
            <div class="flex items-center justify-center h-screen">
                <div class="w-full max-w-4xl p-6 space-y-6">
                    <Card title="Book Your Car" footer="Complete all fields">
                        <div class="space-y-4 text-start">
                            <TextInput
                                labelName="Name"
                                v-model="inputValue"
                                type="text"
                            />
                            <TextInput
                                labelName="Email"
                                v-model="inputValue"
                                type="email"
                            />
                            <TextInput
                                labelName="Phone Number"
                                v-model="inputValue"
                                type="text"
                            />
                            <DropDown 
                                labelName="Car Model" 
                                :items="['Toyota', 'Mazda', 'BMW']" 
                            />
                            <TextInput
                                labelName="Car Year"
                                v-model="inputValue"
                                type="date"
                            />
                        </div>
                        <template #footer>
                            <router-link 
                                to="/" 
                                class="flex gap-2 justify-center rounded-full"
                                tag="button"
                            >
                                <button class="bg-sky-600 text-white px-6 py-2 rounded-lg hover:bg-lightblue-700">
                                    Book
                                </button>
                            </router-link>
                        </template>
                    </Card>
                </div>
            </div>
        </div>
    </div>
  <!-- </Layout> -->
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
