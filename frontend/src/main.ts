import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios';
import './assets/main.css';

axios.defaults.baseURL = 'http://127.0.0.1:8000/api/';

const app = createApp(App);
app.config.globalProperties.$axios = axios; // Make Axios globally available
app.mount('#app');
