<template>
  <div>
    <h1>Car Parts</h1>
    <ul>
      <li v-for="part in carParts" :key="part.id">
        <strong>{{ part.car_name }}:</strong> {{ part.part_name }} - {{ part.interval }} km
      </li>
    </ul>
  </div>
</template>

<script>
import { getCarParts } from "@/api/carParts";

export default {
  data() {
    return {
      carParts: [],
    };
  },
  async created() {
    this.carParts = await getCarParts();
  },
};
</script>
