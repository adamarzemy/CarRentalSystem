<script setup lang="ts">
import Layout from '@layouts/auth/Layout.vue';
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import { useStaffProfileStore } from '@store/staff';
import { Staff } from '@types/modules/staff';
import TextInput from '@components/TextInput.vue';
import Button from '@components/Button.vue';
import ButtonGroup from '@components/ButtonGroup.vue';
import { useToast } from '@lib/ui/toast/use-toast'; 


const staffProfileStore = useStaffProfileStore();
const { toast } = useToast();
const staffProfile = ref<Staff>(staffProfileStore.getStaffProfile);
const router = useRouter();

async function handleSubmit() :Promise<void>{
    try {
        // const result :Promise<any> = await userStore.login(user);
        const result = await staffProfileStore.editStaffProfile(staffProfile.value);
        toast({
            title: 'Edit Profile successful',
            description: 'Thank you',
            variant: 'default',
        });
        console.log('Edit Profile successful:', result);
        router.push({ name: 'ProfilePage' });
    } catch (error) {
        toast({
            title: 'Edit Profile failed',
            description: 'Please try again later',
            variant: 'destructive',
        });
        console.error("Edit Profile failed:", error);
    }
}

</script>

<template>
    <form @submit.prevent="handleSubmit">
        <div id="profile-body" class="container mx-5 my-4">
            <div class="grid grid-cols-12 gap-4 py-2">
            <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
                <div class="grid grid-cols-12 gap-4">
                <div class="col-span-12 sm:col-span-12 md:col-span-4">
                    <label class="text-teal-600 block w-full">First Name:</label>
                </div>
                <div class="col-span-12 sm:col-span-12 md:col-span-8">
                    <TextInput
                        v-model="staffProfile.first_name"
                        type="text"
                    />
                </div>
                </div>
            </div>
            <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
                <div class="grid grid-cols-12 gap-4">
                <div class="col-span-12 sm:col-span-12 md:col-span-4">
                    <label class="text-teal-600 block w-full">Last Name:</label>
                </div>
                <div class="col-span-12 sm:col-span-12 md:col-span-8">
                    <TextInput
                        v-model="staffProfile.last_name"
                        type="text"
                    />
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
                    <TextInput
                        v-model="staffProfile.email"
                        type="text"
                    />
                </div>
                </div>
            </div>
            <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
                <div class="grid grid-cols-12 gap-4">
                <div class="col-span-12 sm:col-span-12 md:col-span-4">
                    <label class="text-teal-600 block w-full">Phone Number:</label>
                </div>
                <div class="col-span-12 sm:col-span-12 md:col-span-8">
                    <TextInput
                        v-model="staffProfile.phone_no"
                        type="text"
                    />
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
                    <TextInput
                        v-model="staffProfile.staff_id"
                        type="text"
                        :readonly="true"
                    />
                </div>
                </div>
            </div>
            <div class="col-span-12 sm:col-span-12 md:col-span-12 py-2">
                <div class="grid grid-cols-12 gap-4">
                <div class="col-span-12 sm:col-span-12 md:col-span-4">
                    <label class="text-teal-600 block w-full">Hire Date:</label>
                </div>
                <div class="col-span-12 sm:col-span-12 md:col-span-8">
                    <TextInput
                        v-model="staffProfile.hire_date"
                        type="text"
                        :readonly="true"
                    />
                </div>
                </div>
            </div>
            </div> 
            <div class="flex justify-center">
                <!-- <Button bgColor="bg-red-500" textColor="text-black" btnHover="hover:text-red-800" /> -->
                <Button type="submit"/>
            </div> 
        </div>
    </form>
</template>
