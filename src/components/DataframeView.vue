<script setup>
const props = defineProps({
    headers: Array,
    items: Array,
    search: String,
});

</script>

<template>
    <div>
      <v-data-table
          :items="items || []"
          :headers="headers"
          class="w-100"
          hide-default-footer
          density="compact"
          :search="search ? search.toLowerCase() : ''"
      >
        <template v-slot:item="{ item, index }">
          <tr :class="{'font-weight-bold': index === items.length - 1}">
            <td>{{ item.nature || item.month }}</td>
            <td class="text-right">{{ item.committed }}</td>
            <td class="text-right">{{ item.liquidated }}</td>
          </tr>
        </template>
      </v-data-table>
    </div>
</template>

<style scoped>
</style>