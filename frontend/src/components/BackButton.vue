<script setup lang="ts">
import ArrowLeftIcon from '@icons/ArrowLeftIcon.vue';
import { useRouter } from 'vue-router';

// Get the router instance
const router = useRouter();

const goBack = () => {
  router.go(-1);  // Goes back to the previous page
}

</script>

<template>
    <button @click="goBack" class="text-black hover:text-teal-500 flex justify-between items-center">
        <ArrowLeftIcon class="me-2"/>
        <span>Back</span>
    </button>
</template>