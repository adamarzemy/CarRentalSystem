<template>
    <div class="inline-flex rounded-md shadow-sm" role="group">
        <slot></slot>
    </div>
</template>
  
<script setup lang="ts">
const handleAction = (action: string) => {
    console.log(`${action} button clicked`);
}

</script>
  