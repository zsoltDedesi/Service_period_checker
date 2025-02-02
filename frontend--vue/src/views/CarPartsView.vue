<template>
  <div class="car-parts-view">
    <h1>Car Parts List</h1>
    <p v-if="loading">Loading car parts...</p>
    <p v-if="error" class="error-message">{{ error }}</p>
    <table v-if="carParts.length > 0" class="car-parts-table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Car Name</th>
          <th>Part Name</th>
          <th>Interval</th>
          <th>Last Replacement</th>
          <th>Notes</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="part in carParts" :key="part.id">
          <td>{{ part.id }}</td>
          <td>{{ part.car_name }}</td>
          <td>{{ part.part_name }}</td>
          <td>{{ part.interval }}</td>
          <td>{{ part.last_replacement }}</td>
          <td>{{ part.notes }}</td>
        </tr>
      </tbody>
    </table>
    <p v-else>No car parts available.</p>
  </div>
</template>

<script>
import { getCarParts } from "@/api/carParts";
// import axios from "axios";

export default {
  name: "CarPartsView",
  data() {
    return {
      carParts: [],
      loading: true,
      error: null,
    };
  },
  methods: {
    async fetchCarParts() {
      try {
        this.carParts = getCarParts()
      } catch (err) {
        this.error = "Failed to load car parts. Please try again later.";
      } finally {
        this.loading = false;
      }
    },
  },
  created() {
    this.fetchCarParts();
  },
};
</script>

<style scoped>
.car-parts-view {
  padding: 2rem;
}

h1 {
  color: #2c3e50;
  text-align: center;
  margin: 1rem 0 2rem 0;
}

.car-parts-table {
  width: 100%;
  border-collapse: collapse;
  margin: 0 auto;
  text-align: left;
}

.car-parts-table th,
.car-parts-table td {
  border: 1px solid #ddd;
  padding: 0.75rem;
}

.car-parts-table th {
  background-color: #cacaca;
  font-weight: bold;
  color: black;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 1rem;
}

</style>
