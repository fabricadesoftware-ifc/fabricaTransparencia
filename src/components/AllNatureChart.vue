<script setup>
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { BarChart } from 'echarts/charts'
import { DatasetComponent, GridComponent, LegendComponent, TooltipComponent } from 'echarts/components'
import VChart, { THEME_KEY } from 'vue-echarts'
import { useAppStore } from '../stores/app'
import { onMounted, provide } from 'vue'
import DataframeView from './DataframeView.vue'

const appStore = useAppStore()

use([
  CanvasRenderer,
  BarChart,
  LegendComponent,
  TooltipComponent,
  DatasetComponent,
  GridComponent,
])

provide(THEME_KEY, 'default')

const headers = [
  { title: 'Natureza', align: 'start', key: 'nature' },
  { title: 'Empenhado (R$)', align: 'end', key: 'committed' },
  { title: 'Liquidado (R$)', align: 'end', key: 'liquidated' },
]
const search = ref('')
</script>

<template>
    <div class="mx-16">
      <TitleSection title="Total de Recursos Empenhados e Liquidados por Natureza de Despesa" />
        <div class="chart-dataset mb-8">
        <v-chart class="chart" :option="appStore.allNaturesChart"/>
        </div>
        <v-text-field
            v-model="search"
            label="Buscar por natureza..."
            prepend-inner-icon="mdi-magnify"
            variant="outlined"
            single-line
        ></v-text-field>
        <DataframeView :headers="headers" :items="appStore.allNaturesDataframe" :search="search"/>
    </div>
  </template>

<style lang="css" scoped>
  .chart-dataset {
    height: 500px;
  }
</style>
