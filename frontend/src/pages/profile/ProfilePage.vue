<script setup lang="ts">
import Layout from '@layouts/auth/Layout.vue';

import { ref } from 'vue';
import { useStaffProfileStore } from '@store/staff';
import Card from '@components/Card.vue'; 
import { Staff } from '@types/modules/staff';
import EditProfileIcon from '@icons/EditProfileIcon.vue';
// import ProfileEditPage from '@profile/ProfileEditPage.vue';

const staffProfileStore = useStaffProfileStore();

const inputValue = ref('');

const name = ref('Taufik')
const readonly = ref<boolean>(true)

const staffProfile = ref<Staff>(staffProfileStore.getStaffProfile);

</script>

<!-- <template>
  <Layout>
    <template #content>
      <div style="margin-top: 4rem;"></div>
      <div class="mx-auto px-4 mb-8">
        <Card>
          <div class="container">
            <div class="flex justify-end">
              <router-link class="flex justify-between hover:text-teal-500" :to="{ name: 'ProfileEditPage' }"><EditProfileIcon class="me-2"/> Edit Profile</router-link>
            </div>
            <div class="flex justify-center items-center pt-8 mb-2">
              <img src="https://avatars.githubusercontent.com/u/97021587?v=4" class="p-1 w-28 h-28 rounded-full ring-2 ring-gray-300 dark:ring-gray-500 mb-4" alt="Avatar" />
            </div>
            <div class="text-center mb-4">
              <span class="mb-2 block text-slate-400">{{ staffProfile.first_name }} {{ staffProfile.last_name }}</span>
              <span class="block text-slate-400">Admin</span>
            </div>
            <hr>
            <div id="profile-body" class="container mx-5 my-4">
              <div class="grid grid-cols-12 gap-4 py-2">
                <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
                  <div class="grid grid-cols-12 gap-4">
                    <div class="col-span-12 sm:col-span-12 md:col-span-4">
                      <label class="text-teal-600 block w-full">First Name:</label>
                    </div>
                    <div class="col-span-12 sm:col-span-12 md:col-span-8">
                      <span class="rounded block w-full text-black">{{ staffProfile.first_name }}</span>
                    </div>
                  </div>
                </div>
                <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
                  <div class="grid grid-cols-12 gap-4">
                    <div class="col-span-12 sm:col-span-12 md:col-span-4">
                      <label class="text-teal-600 block w-full">Last Name:</label>
                    </div>
                    <div class="col-span-12 sm:col-span-12 md:col-span-8">
                      <span class="rounded block w-full text-black">{{ staffProfile.last_name }}</span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="grid grid-cols-12 gap-4 py-2">
                <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
                  <div class="grid grid-cols-12 gap-4">
                    <div class="col-span-12 sm:col-span-12 md:col-span-4">
                      <label class="text-teal-600 block w-full">Email:</label>
                    </div>
                    <div class="col-span-12 sm:col-span-12 md:col-span-8">
                      <span class="rounded block w-full text-black">{{ staffProfile.email }}</span>
                    </div>
                  </div>
                </div>
                <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
                  <div class="grid grid-cols-12 gap-4">
                    <div class="col-span-12 sm:col-span-12 md:col-span-4">
                      <label class="text-teal-600 block w-full">Phone Number:</label>
                    </div>
                    <div class="col-span-12 sm:col-span-12 md:col-span-8">
                      <span class="rounded block w-full text-black">{{ staffProfile.phone_no }}</span>
                    </div>
                  </div>
                </div>
              </div>   
              <div class="grid grid-cols-12 gap-4 py-2">
                <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
                  <div class="grid grid-cols-12 gap-4">
                    <div class="col-span-12 sm:col-span-12 md:col-span-4">
                      <label class="text-teal-600 block w-full">Staff ID:</label>
                    </div>
                    <div class="col-span-12 sm:col-span-12 md:col-span-8">
                      <span class="rounded block w-full text-black">{{ staffProfile.staff_id }}</span>
                    </div>
                  </div>
                </div>
                <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
                  <div class="grid grid-cols-12 gap-4">
                    <div class="col-span-12 sm:col-span-12 md:col-span-4">
                      <label class="text-teal-600 block w-full">Hire Date:</label>
                    </div>
                    <div class="col-span-12 sm:col-span-12 md:col-span-8">
                      <span class="rounded block w-full text-black">{{ staffProfile.hire_date }}</span>
                    </div>
                  </div>
                </div>
              </div>  
            </div>
          </div>
        </Card>
      </div>
    </template>
  </Layout>
</template> -->

<template>
  <div id="profile-body" class="container mx-5 my-4">
    <div class="grid grid-cols-12 gap-4 py-2">
      <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
        <div class="grid grid-cols-12 gap-4">
          <div class="col-span-12 sm:col-span-12 md:col-span-4">
            <label class="text-teal-600 block w-full">First Name:</label>
          </div>
          <div class="col-span-12 sm:col-span-12 md:col-span-8">
            <span class="rounded block w-full text-black">{{ staffProfile.first_name }}</span>
          </div>
        </div>
      </div>
      <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
        <div class="grid grid-cols-12 gap-4">
          <div class="col-span-12 sm:col-span-12 md:col-span-4">
            <label class="text-teal-600 block w-full">Last Name:</label>
          </div>
          <div class="col-span-12 sm:col-span-12 md:col-span-8">
            <span class="rounded block w-full text-black">{{ staffProfile.last_name }}</span>
          </div>
        </div>
      </div>
    </div>
    <div class="grid grid-cols-12 gap-4 py-2">
      <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
        <div class="grid grid-cols-12 gap-4">
          <div class="col-span-12 sm:col-span-12 md:col-span-4">
            <label class="text-teal-600 block w-full">Email:</label>
          </div>
          <div class="col-span-12 sm:col-span-12 md:col-span-8">
            <span class="rounded block w-full text-black">{{ staffProfile.email }}</span>
          </div>
        </div>
      </div>
      <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
        <div class="grid grid-cols-12 gap-4">
          <div class="col-span-12 sm:col-span-12 md:col-span-4">
            <label class="text-teal-600 block w-full">Phone Number:</label>
          </div>
          <div class="col-span-12 sm:col-span-12 md:col-span-8">
            <span class="rounded block w-full text-black">{{ staffProfile.phone_no }}</span>
          </div>
        </div>
      </div>
    </div>   
    <div class="grid grid-cols-12 gap-4 py-2">
      <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
        <div class="grid grid-cols-12 gap-4">
          <div class="col-span-12 sm:col-span-12 md:col-span-4">
            <label class="text-teal-600 block w-full">Staff ID:</label>
          </div>
          <div class="col-span-12 sm:col-span-12 md:col-span-8">
            <span class="rounded block w-full text-black">{{ staffProfile.staff_id }}</span>
          </div>
        </div>
      </div>
      <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
        <div class="grid grid-cols-12 gap-4">
          <div class="col-span-12 sm:col-span-12 md:col-span-4">
            <label class="text-teal-600 block w-full">Hire Date:</label>
          </div>
          <div class="col-span-12 sm:col-span-12 md:col-span-8">
            <span class="rounded block w-full text-black">{{ staffProfile.hire_date }}</span>
          </div>
        </div>
      </div>
    </div>  
  </div>
</template>
