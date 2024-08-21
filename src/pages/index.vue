<template>
  <div class="mx-4 mt-16">
    <p class="text-caption position-fixed top-0 left-0 pa-2 text-red">
      {{ appStore.state.datas ? 'Data loaded' : 'Loading data...' }}
    </p>
    <HeaderComp />
    <GlobalIndicators />
    <MainChart />
    <AllNatureChart />
    <MainTabs />
  </div>
</template>

<script setup>
import { useAppStore } from '@/stores/app';
import MainTabs from '@/components/MainTabs.vue';

const appStore = useAppStore();

onMounted(async () => {
  await appStore.getCharts();
});
</script>
