<script setup lang="ts">
const model = defineModel({
    type: null,
    required: true,
});
defineProps({
    labelName: {
        type: String,
        required: true,
    },
    type: {
        type: String,
        default: 'text'
    },
    message: String
})
</script>

<template>
    <div class="mb-6">
        <label>{{ labelName }}</label>
        <input :type="type" v-model="model" :class="[
            'border border-black focus:outline-none focus:ring-2 focus:ring-black', // Default black border
            message ? '!ring-2 ring-red-500' : '' // Red ring when there's a message
        ]"/>
        <small class="error text-red-500" v-if="message">{{ message }}</small>
    </div>
</template>
