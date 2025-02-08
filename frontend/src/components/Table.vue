<script setup lang="ts">
import TableHeader from './TableHeader.vue';
import TableRow from './TableRow.vue';
import { ref } from 'vue';

type RowType = { ID: number; Name: string; Description: string; Date: string; Amount: number; };

const headers = [
  { key: 'ID', label: 'ID', sortable: true },
  { key: 'Name', label: 'Name', sortable: true },
  { key: 'Description', label: 'Description', sortable: false },
  { key: 'Date', label: 'Date', sortable: true },
  { key: 'Amount', label: 'Amount', sortable: true },
  { key: 'Actions', label: 'Actions', sortable: false },
];

const rows = [
  { ID: 1, Name: 'John Doe', Description: 'Test user', Date: '2023-12-01', Amount: 150 },
  { ID: 2, Name: 'Jane Smith', Description: 'Another test user', Date: '2023-12-02', Amount: 200 },
  { ID: 3, Name: 'Alice Johnson', Description: 'A third test user', Date: '2023-12-03', Amount: 250 },
];

const sortConfig = ref({ key: '', direction: '' });

const sortRows = (key: keyof RowType) => {
  if (sortConfig.value.key === key) {
    sortConfig.value.direction = sortConfig.value.direction === 'asc' ? 'desc' : 'asc';
  } else {
    sortConfig.value.key = key;
    sortConfig.value.direction = 'asc';
  }

  rows.sort((a, b) => {
    const valA = a[key];
    const valB = b[key];

    if (valA === valB) return 0;

    if (sortConfig.value.direction === 'asc') {
      return valA > valB ? 1 : -1;
    } else {
      return valA < valB ? 1 : -1;
    }
  });
};
</script>

<template>
  <div class="overflow-x-auto">
    <table class="table-auto border-collapse border border-gray-300 w-full text-left">
      <!-- Table Header -->
      <thead class="bg-gray-100 text-gray-700">
        <TableHeader :headers="headers" :sortConfig="sortConfig" @sort="sortRows" />
      </thead>
      <!-- Table Body -->
      <tbody>
        <TableRow v-for="row in rows" :key="row.ID" :row="row" />
      </tbody>
    </table>
  </div>
</template>
