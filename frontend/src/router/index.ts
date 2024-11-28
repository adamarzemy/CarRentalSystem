import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: () => import('@pages/HomePage.vue'), 
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: () => import('@pages/LoginPage.vue'),
  },
  {
    path: '/register',
    name: 'RegisterPage',
    component: () => import('@pages/RegisterPage.vue'),
  },
  {
    path: '/dashboard',
    name: 'DashboardPage',
    component: () => import('@pages/DashboardPage.vue'),
  },
  {
    path: '/booking',
    name: 'UserBookingPage',
    component: () => import('@pages/user/BookingPage.vue'), 
  },
];

// Create router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
