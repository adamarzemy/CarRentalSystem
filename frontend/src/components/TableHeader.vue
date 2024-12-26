<script setup lang="ts">
import { defineProps, defineEmits } from 'vue';

defineProps({
  headers: Array,
  sortConfig: Object,
});

type Header = {
  key: string;
  label: string;
  sortable: boolean;
};

const headers: Header[] = [
  { key: 'ID', label: 'ID', sortable: true },
  { key: 'Name', label: 'Name', sortable: true },
  { key: 'Description', label: 'Description', sortable: false },
  { key: 'Date', label: 'Date', sortable: true },
  { key: 'Amount', label: 'Amount', sortable: true },
];

defineEmits(['sort']);
</script>

<template>
  <tr>
    <th
      v-for="header in headers"
      :key="header.key"
      class="border border-gray-300 px-4 py-2 cursor-pointer"
      @click="header.sortable ? $emit('sort', header.key) : null"
    >
      <div class="flex items-center justify-between">
        <span>{{ header.label }}</span>
        <span v-if="header.sortable" class="ml-2">
          <i
            v-if="sortConfig.key === header.key && sortConfig?.direction === 'asc'"
            class="fas fa-arrow-up text-blue-500"
          ></i>
          <i
            v-if="sortConfig.key === header.key && sortConfig?.direction === 'desc'"
            class="fas fa-arrow-down text-blue-500"
          ></i>
          <i
            v-if="sortConfig?.key !== header.key"
            class="fas fa-arrows-alt-v text-gray-400"
          ></i>
        </span>
      </div>
    </th>
  </tr>
</template>
