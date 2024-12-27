<script setup lang="ts">
import Layout from '@layouts/auth/Layout.vue';
import { ref } from 'vue';
import { useVehicleStore } from '@store/vehicle';
import Card from '@components/Card.vue'; 
import Table from '@components/Table.vue';
import TableLib from '@components/TableLib.vue';
import { useCustomerStore } from '@store/customer';
import { Customer } from '@types/modules/customer';

const customerStore = useCustomerStore();
const customers = ref<Customer[]>(customerStore.getCustomers);
const columns: Array<string> = ['Name', 'Email', 'Address', 'Date Of Birth', 'License Type'];
</script>

<template>
  <TableLib :data="customers" :columns="columns" dataType="Customer" />
</template>
