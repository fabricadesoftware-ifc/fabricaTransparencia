<script setup>
const props = defineProps(['value', 'label', 'isNegative']);
</script>

<template>
    <h4 class="text-h4 font-weight-bold" :class="{'text-red' : value < 0 || isNegative}">
        R$ {{ value }}
    </h4>
    <h6 class="pt-4 text-subtitle-2 text-grey font-italic font-weight-regular">
        {{ label }}
    </h6>
</template>