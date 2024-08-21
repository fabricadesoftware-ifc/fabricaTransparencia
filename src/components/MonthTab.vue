<script setup>
import { use } from "echarts/core";
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  GridComponent,
  LegendComponent,
  TooltipComponent,
} from "echarts/components";
import VChart, { THEME_KEY } from "vue-echarts";
import { useAppStore } from "../stores/app";

const appStore = useAppStore();
const monthsInput = ref([])

use([
  CanvasRenderer,
  PieChart,
  LegendComponent,
  TooltipComponent,
  GridComponent,
]);

provide(THEME_KEY, "default");
</script>

<template>
  <v-row class="pb-6">
    <v-col cols="12" md="9">
      <v-autocomplete
          clearable
          chips
          label="Selecione os Meses"
          :items="appStore.months"
          multiple
          variant="outlined"
          hide-details
          v-model="monthsInput"
          class="pt-3"
      ></v-autocomplete>
    </v-col>
    <v-col cols="12" md="3">
      <v-btn
        text="Filtrar"
        class="mt-3 py-7"
        color="primary"
        block
        @click="appStore.filteringMonths(monthsInput)"
      ></v-btn>
    </v-col>
  </v-row>
  {{ appStore.datas?.byMonthChart?.["Filtros"] }}
  {{ monthsInput }}
  <div class="chart-pie">
    <v-chart class="chart" :option="appStore.byMonthChart" />
  </div>
</template>

<style scoped>
.chart-pie {
    height: 500px;
}
</style>