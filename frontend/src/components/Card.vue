<script setup lang="ts">
import { defineProps } from 'vue';

defineProps({
  title: {
    type: String,
    default: '',
  },
  footer: {
    type: String,
    default: '',
  },
});
</script>

<template>
  <div class="bg-white border border-gray-200 rounded-lg shadow-md p-4" style="min-height: 750px;">
    <div v-if="title" class="mb-4 text-lg font-semibold text-gray-700">
      {{ title }}
    </div>
    <div class="card-body">
      <slot />
    </div>
    <div v-if="footer" class="mt-4 text-sm text-gray-500 border-t pt-2">
      <slot name="footer"></slot>
    </div>
  </div>
</template>