<script setup lang="ts">
// const model = defineModel({
//     type: null,
//     required: true,
// });
defineProps({
    bgColor: {
        type: String,
        default: 'bg-teal-500'
    },
    textColor: {
        type: String,
        default: 'text-white'
    },
    btnHover: {
        type: String,
        default: 'hover:text-teal-800'
    },
    btnLabel: {
        type: String,
        default: 'Submit'
    },
    btnType: {
        type: String as () => 'button' | 'submit' | 'reset',
        default: 'button'
    },
    isGroup: {
        type: Boolean,
        default: false
    }
})

</script>

<template>
    <button 
        class="px-3 py-2"
        :class="[bgColor, textColor, btnHover,
            isGroup ? '' : 'rounded-md'
        ]"
        :type="btnType"
    >
    {{ btnLabel }}
    </button>

    <!-- example is isGroup in other vue file
    <ButtonGroup>
        <Button type="submit" :isGroup="true"/>
        <Button type="submit" :isGroup="true"/>
        <Button type="submit" :isGroup="true"/>
    </ButtonGroup>  -->
</template>