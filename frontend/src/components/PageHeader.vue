<script setup lang="ts">
import { defineProps } from 'vue';
import BreadCrumb from '@components/BreadCrumb.vue';

// Props for customization
defineProps({
  title: {
    type: String,
    required: true,
  },
  subtitle: {
    type: String,
    required: false,
    default: '',
  },
  actions: {
    type: Array as () => { label: string; action: () => void; styleClass?: string }[],
    required: false,
    default: () => [],
  },
});
</script>

<template>
    <div class="bg-transparent py-4 px-6">
        <div class="flex items-center justify-between">
        <!-- Title and Subtitle -->
            <div>
                <h1 class="text-2xl font-semibold text-gray-800">{{ title }}</h1>
                <p v-if="subtitle" class="text-gray-600">{{ subtitle }}</p>
            </div>

            <!-- Actions -->
            <div v-if="actions.length > 0" class="flex space-x-2">
                <button
                v-for="(action, index) in actions"
                :key="index"
                :class="action.styleClass || 'bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition'"
                @click="action.action"
                >
                {{ action.label }}
                </button>
            </div>
            <!-- <router-view/> -->
            <BreadCrumb />
        </div>
    </div>
</template>

<style scoped>
</style>
