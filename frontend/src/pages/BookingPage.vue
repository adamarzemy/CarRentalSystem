<script setup lang="ts">
import Layout from '@layouts/auth/Layout.vue';

import { ref } from 'vue';
import { useVehicleStore } from '@store/vehicle';
import Card from '@components/Card.vue'; 
import Table from '@components/Table.vue';

const vehicleStore = useVehicleStore();
const vehicles :any = vehicleStore.getVehicles;

</script>

<template>
  <Layout>
    <template #content>
        <div style="margin-top: 4rem;"></div>
        <div class="max-w-screen-xl mx-auto px-4">
            <Card title="Vehicle" footer="vehicles">
                <Table/>
            </Card>
        </div>
    </template>
  </Layout>
</template>
