<template>
  <div>
    <!-- <h1>{{ message }}</h1> -->
    <h1 class="text-3xl font-bold underline">
    {{ message }}
  </h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: '',
    };
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/hello/') 
      .then(response => {
        this.message = response.data.message;
      })
      .catch(error => {
        console.error(error);
      });
  },
};
</script>
