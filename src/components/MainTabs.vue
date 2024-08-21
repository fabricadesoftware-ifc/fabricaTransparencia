<script setup>
const tab = ref('months')
</script>

<template>
    <v-card class="w-100 px-16 mt-8" variant="flat">
      <v-tabs
        v-model="tab"
        color="primary"
      >
        <v-tab value="months">Buscar Por Mês</v-tab>
        <v-tab value="natures">Buscar por Natureza</v-tab>
        <v-tab value="datas">Ver Dados Brutos</v-tab>
      </v-tabs>
  
      <v-card-text class="px-0 mx-0">
        <v-tabs-window v-model="tab">
          <v-tabs-window-item value="months" class="mx-0 px-0">
            <MonthTab />
          </v-tabs-window-item>
          <v-tabs-window-item value="natures">
            natures
          </v-tabs-window-item>
          <v-tabs-window-item value="datas">
            datas
          </v-tabs-window-item>
        </v-tabs-window>
      </v-card-text>
    </v-card>
</template>