<script>
import { useAppStore } from '@/stores/app';

const appStore = useAppStore()
</script>

<template>
    <div>
        <v-autocomplete
            clearable
            chips
            label="Selecione os Meses"
            :items="appStore.months"
            multiple
        ></v-autocomplete>
    </div>
</template>