<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router';
import { computed } from 'vue';

const route = useRoute();
const router = useRouter();

const breadcrumbs = computed(() => {
  const matchedRoutes = route.matched;
  return matchedRoutes.map((route) => ({
    label: route.meta.breadcrumb || route.name,
    path: route.path,
  }));
});
</script>

<template>
  <nav class="flex items-center space-x-2 text-gray-600">
    <template v-for="(breadcrumb, index) in breadcrumbs" :key="breadcrumb.path">
      <router-link
        v-if="index < breadcrumbs.length - 1"
        :to="breadcrumb.path"
        class="text-blue-500 hover:underline"
      >
        {{ breadcrumb.label }}
      </router-link>
      <span v-else>{{ breadcrumb.label }}</span>
      <span v-if="index < breadcrumbs.length - 1">/</span>
    </template>
  </nav>
</template>
