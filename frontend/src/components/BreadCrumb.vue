<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router';
import { computed } from 'vue';

const route = useRoute();
const router = useRouter();

const breadcrumbs = computed(() => {
  const matchedRoutes = route.matched;
  return matchedRoutes.map((route) => ({
    label: route.meta.breadcrumb || null,
    path: route.path,
  }));
});
</script>

<template>
  <nav class="flex items-center space-x-2 text-gray-600">
    <template v-for="(breadcrumb, index) in breadcrumbs" :key="breadcrumb.path">
      <!-- Only render breadcrumb if label is available -->
      <template v-if="breadcrumb.label">
        <router-link
          v-if="index < breadcrumbs.length - 1"
          :to="breadcrumb.path"
          class="text-blue-500 hover:underline"
        >
          {{ breadcrumb.label }}
        </router-link>
        <span v-else>{{ breadcrumb.label }}</span>

        <!-- Only show the separator if the next breadcrumb label is not null -->
        <span v-if="breadcrumbs[index + 1]?.label">/</span>
      </template>
    </template>
  </nav>
</template>
