<template>
    <div class="w-full bg-gray-100 ">
        <div class="flex justify-between items-center h-[50px]">
            <div class="p-4 cursor-pointer  hover:bg-gray-50" @click="clickHambuger">
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                    class="w-6 h-6"
                >
                    <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M4 6h16M4 12h16m-7 6h7"
                    />
                </svg>
            </div>
            <div class="py-2">
                <!-- <InputText type="text" v-model="value" class="h-[40px]" placeholder="Search.." /> -->
                text input here maybe
            </div>
            <div class="flex space-x-3 items-center justify-center px-3">
                <div class="text-md">
                    Admin
                </div>
                <Avatar icon="pi pi-user" class="mr-2" style="background-color:#9c27b0; color: #ffffff" shape="circle" @click="toggle" aria-haspopup="true" aria-controls="overlay_menu" />
                <Menu id="overlay_menu" ref="menu" :model="items" :popup="true" />
            </div>
        </div>
    </div>
</template>
  
<script>
  export default {
    props: {
      dataOpenSideBar: Boolean,
      clickHambuger: Function
    },
    data() {
      return {
        items: [
          {
            label: 'Logout',
            icon: 'pi pi-refresh',
            command: () => {
              this.$toast.add({ severity: 'success', summary: 'Updated', detail: 'Data Updated', life: 3000 });
            }
          },
          {
            label: 'Change Password',
            icon: 'pi pi-times',
            command: () => {
              this.$toast.add({ severity: 'warn', summary: 'Delete', detail: 'Data Deleted', life: 3000 });
            }
          },
        ]
      }
    },
    methods: {
      toggle(event) {
        this.$refs.menu.toggle(event);
      },
    }
  }
</script>