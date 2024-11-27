<script setup lang="ts">
import Sidebar from '../components/Sidebar.vue';
import Navbar from '../components/Navbar.vue';
import { ref } from 'vue';

const openSidebar = ref(true)
const toggleSidebar = () => {
  openSidebar.value = !openSidebar.value
}
</script>

<template>
  <!-- <Sidebar/> -->
  <div class="w-full h-full flex">
    <Sidebar :dataOpenSideBar="openSidebar" />
    <div class="w-full h-full">
      <Navbar :dataOpenSideBar="openSidebar" :clickHambuger="toggleSidebar" />
      <div class="w-full h-[calc(100vh-50px)]">
        <!-- <router-view></router-view> -->
      </div>
    </div>
  </div>
</template>