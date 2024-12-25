<script setup lang="ts">
import Layout from '@layouts/auth/Layout.vue';

import { ref, onMounted } from 'vue';
import { FilterMatchMode } from '@primevue/core/api';
import { useVehicleStore } from '@store/vehicle';
import { VehicleTest } from '@types/vehicle';
import Card from '@components/Card.vue'; 
import DataTable from 'datatables.net-dt';
// import { CustomerService } from '@/service/CustomerService';


const vehicleStore = useVehicleStore();
const vehicles :any = vehicleStore.getVehicles;


const getVehicles = (vehicles: VehicleTest[]) => {
  return vehicles.map((d) => {
    // Assuming `date` is part of the vehicle object, or you need to add it.
    if (d.date) {
      d.date = new Date(d.date); // Convert date if it exists
    }
    return d;
  });
};

const getSeverity = (status: string): "danger" | "success" | "info" | "warn" | "secondary" | "contrast" | undefined => {
    switch (status) {
        case 'unqualified':
            return 'danger';

        case 'qualified':
            return 'success';

        case 'new':
            return 'info';

        case 'used':
            return 'warn';

        case 'renewal':
            return 'danger';
    }
}

onMounted(() => {
//   table = new DataTable('#myTable');
});

let table = new DataTable('#myTable');


</script>

<template>
  <Layout>
    <template #content>
        <Card title="Vehicle" footer="vehicles">
            <table id="myTable" class="display">
                <thead>
                    <tr>
                        <th class="text-left">Brand</th>
                        <th class="text-left">Model</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(vehicle, index) in vehicles" :key="index">
                        <td class="text-left">{{ vehicle.brand }}</td>
                        <td class="text-left">{{ vehicle.model }}</td>
                    </tr>
                </tbody>
            </table>
        </Card>
    </template>
  </Layout>
</template>
