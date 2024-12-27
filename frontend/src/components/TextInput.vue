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
    message: String,
    readonly: {
        type: Boolean,
        default: false
    }
})
</script>

<template>
    <div class="mb-6 flex mx-4">
        <label class="text-black me-2 w-1/5">{{ labelName }}</label>
        <input 
            :type="type" 
            v-model="model" 
            :class="[
                readonly 
                    ? '' // Default black border when readonly
                    : 'border focus:outline-none focus:ring-2 focus:ring-black',
                message 
                    ? '!ring-2 ring-red-500' // Red ring when there's a message
                    : 'border-black' // Black border when no message
            ]" 
            class="rounded w-2/5 text-black" 
            :readonly="readonly"
        />
        <small class="error text-red-500" v-if="message">{{ message }}</small>
    </div>
</template>
