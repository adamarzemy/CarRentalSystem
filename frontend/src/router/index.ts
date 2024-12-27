import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@store/auth';
import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'HomePage',
    component: () => import('@pages/HomePage.vue'), 
    meta: { breadcrumb: 'Home', title: 'Home' },
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: () => import('@pages/LoginPage.vue'),
    meta: { breadcrumb: 'Login', title: 'Login' },
  },
  {
    path: '/register',
    name: 'RegisterPage',
    component: () => import('@pages/RegisterPage.vue'),
    meta: { breadcrumb: 'Register', title: 'Register' },
  },
  {
    path: '/dashboard',
    name: 'DashboardPage',
    component: () => import('@pages/DashboardPage.vue'),
    meta: { breadcrumb: 'Dashboard', title: 'Dashboard' },
    // children: [
    //   {
    //     path: 'booking',
    //     name: 'BookingPage',
    //     component: () => import('@pages/BookingPage.vue'),
    //     meta: { breadcrumb: 'Booking' },
    //   }
    // ]
  },
  {
    path: '/admin/profile',
    name: 'ProfilePage',
    component: () => import('@pages/ProfilePage.vue'),
    meta: { breadcrumb: 'Profile', title: 'Profile' },
  },
  {
    path: '/admin/customer',
    name: 'CustomerPage',
    component: () => import('@pages/CustomerPage.vue'),
    meta: { breadcrumb: 'Customer', title: 'Customer' },
  },
  {
    path: '/admin/booking',
    name: 'BookingPage',
    component: () => import('@pages/BookingPage.vue'),
    meta: { breadcrumb: 'Booking', title: 'Booking' },
  },
  {
    path: '/admin/billing',
    name: 'BillingPage',
    component: () => import('@pages/BillingPage.vue'),
    meta: { breadcrumb: 'Billing', title: 'Billing' },
  },
  {
    path: '/admin/discount',
    name: 'DiscountPage',
    component: () => import('@pages/DiscountPage.vue'),
    meta: { breadcrumb: 'Discount', title: 'Discount' },
  },
  {
    path: '/admin/vehicle',
    name: 'VehiclePage',
    component: () => import('@pages/VehiclePage.vue'),
    meta: { breadcrumb: 'Vehicle', title: 'Vehicle' },
  },
  {
    path: '/booking',
    name: 'UserBookingPage',
    component: () => import('@pages/user/BookingPage.vue'), 
    meta: { breadcrumb: 'Booking', title: 'Booking' },
  },
  // {
  //   path: '/:pathMatch(.*)*',
  //   name: 'NotFound',
  //   beforeEnter: (to, from, next) => {
  //     const authStore = useAuthStore();
  //     const isAuth = authStore.getIsAuth; // Adjust based on your auth logic.
  //     if (isAuth) {
  //       next({ name: 'DashboardPage' });
  //     } else {
  //       next({ name: 'HomePage' });
  //     }
  //   },
  // },
  {
    path: '/:pathMatch(.*)*',
    name: 'NotFound',
    redirect: (to) => {
      const authStore = useAuthStore();
      const isAuth = authStore.getIsAuth; // Replace with your auth logic
      return isAuth ? { name: 'DashboardPage' } : { name: 'HomePage' };
    },
  },
];

// Create router instance
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
