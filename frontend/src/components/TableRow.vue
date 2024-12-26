<script setup lang="ts">
import { defineProps } from 'vue';

defineProps({
  row: Object,
});
</script>

<template>
  <tr class="hover:bg-gray-100">
    <td v-for="(value, key) in row" :key="key" class="border border-gray-300 px-4 py-2">
      {{ value }}
    </td>
  </tr>
</template>
