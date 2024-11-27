<script setup lang="ts">
import { defineModel } from 'vue'

const model = defineModel({
    required: true,
});
defineProps({
    labelName: {
        type: String,
        required: true,
    },
    name: {
        type: String,
        required: true,
    },
    items: {
        type: Array,
        required: true,
    },
    message: {
        type: String,
        default: null,
    },
});
</script>

<template>
    <div class="mb-6">
        <label>{{ labelName }}</label>
        <select v-model="model" :class="{'!ring-2 ring-red-500': message}">
            <option disabled value="">{{ name }}</option>
            <option v-for="(item, index) in items" :key="index" :value="item">
                {{ item }}
            </option>
        </select>
        <small class="error text-red-500" v-if="message">{{ message }}</small>
    </div>
</template>
