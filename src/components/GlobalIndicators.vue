<script setup>
import { useAppStore } from '@/stores/app';

const appStore = useAppStore();
</script>

<template>
  <div class="mx-16 mt-8">
    <h4 class="text-subtitle-1 text-grey pb-8">Indicadores Gerais</h4>
    <v-row>
      <v-col cols="12" md="4">
        <IndicatorItem :value="appStore.committed" label="Montante Empenhado" />
      </v-col>
      <v-col cols="12" md="4">
        <IndicatorItem :value="appStore.settled" label="Montante Liquidado" />
      </v-col>
      <v-col cols="12" md="4">
        <IndicatorItem :isNegative="true" :value="appStore.balance" label="Montante Pendente de Liquidação" />
      </v-col>
    </v-row>
  </div>
</template>
