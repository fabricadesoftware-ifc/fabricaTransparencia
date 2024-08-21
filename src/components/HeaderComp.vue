<script setup>
const school = ref(['Araquari'])
const state = ref(['Santa Catarina'])
</script>

<template>
  <header class="mx-16 mt-16 border-b-thin pb-2">
    <NavComp />
    <h1 class="text-h3 font-weight-bold">
      Painel de Transparência Financeira do
      <span class="text-green-darken-3">IFC - Campus Araquari</span>
    </h1>
    <p class="py-6 text-grey">
      Este projeto tem por objetivo possibilitar à comunidade o acompanhamento
      da execução do orçamento do campus. As informações são apresentadas
      considerando, ao longo do tempo, os valores de Despesas Empenhadas e
      Despesas Liquidadas.
    </p>
    <v-row>
      <v-col cols="12" md="3">
        <v-autocomplete
          v-model="state"
          :items="['Santa Catarina', '...']"
          label="Selecione o Estado"
          variant="outlined"
        />
      </v-col>
      <v-col cols="12" md="3">
        <v-autocomplete
          v-model="school"
          :items="['Araquari', '...']"
          label="Selecione o Campus"
          variant="outlined"
        />
      </v-col>
    </v-row>
  </header>
</template>
