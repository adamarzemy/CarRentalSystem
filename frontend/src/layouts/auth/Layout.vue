<script setup lang="ts">
import Sidebar from '@components/Sidebar.vue';
import Navbar from '@components/Navbar.vue';
import { ref } from 'vue';

const isAuth = ref<boolean>(true)
const openSidebar = ref<boolean>(true)
const toggleSidebar = () => {
  openSidebar.value = !openSidebar.value
}
</script>

<template>
  <!-- <Sidebar/> -->
  <div class="w-full h-full flex">
    <Sidebar :dataOpenSideBar="openSidebar" />
    <div class="w-full h-full">
      <Navbar :dataOpenSideBar="openSidebar" :clickHambuger="toggleSidebar" :isAuth="isAuth"/>
      <div class="w-full h-[calc(100vh-50px)]">
        <!-- <router-view></router-view> -->
      </div>
    </div>
  </div>
</template>