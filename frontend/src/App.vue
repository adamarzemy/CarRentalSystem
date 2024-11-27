<template>
  <div id="app">
    <HelloWorld />
  </div>
  <div class="bg-blue-500 text-white p-4">
    Tailwind Added!
  </div>

</template>

<script>
import HelloWorld from './components/HelloWorld.vue';

export default {
  components: {
    HelloWorld,
  },
};
</script>
