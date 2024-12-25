import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@store/auth';

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
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    beforeEnter: (to, from, next) => {
      const authStore = useAuthStore();
      const isAuth = authStore.getIsAuth; // Adjust based on your auth logic.
      if (isAuth) {
        next({ name: 'DashboardPage' });
      } else {
        next({ name: 'HomePage' });
      }
    },
  },
];

// Create router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
