<script setup lang="ts">
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  message: {
    type: String,
    required: true,
  },
  type: {
    type: String,
    required: true,
    validator: (value: string) => ['success', 'error'].includes(value),
  },
});

const emit = defineEmits(['close']);
</script>

<template>
  <div
    :class="[
      'p-4 rounded-lg flex justify-between items-center mb-4',
      type === 'success' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
    ]"
  >
    <span>{{ message }}</span>
    <button @click="$emit('close')" class="ml-4 text-lg font-bold text-gray-700 hover:text-gray-500">
      &times;
    </button>
  </div>
</template>

<style scoped>
button {
  cursor: pointer;
}
</style>
