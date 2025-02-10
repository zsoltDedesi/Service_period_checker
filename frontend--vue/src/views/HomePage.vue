<template>
  <div class="homepage">
    <h1>Welcome to the Car Service Manager!</h1>
    <p>
      This application helps you manage car parts and their maintenance schedules.
      You can view a list of parts, add new parts, and track replacements to keep your car in perfect condition.
    </p>
    <div class="actions">
      <router-link to="/car-parts" class="action-link">View Car Parts</router-link>
      <router-link to="/add-car-part" class="action-link">Add New Car Part</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage",
};
</script>

<style scoped>
.homepage {
  text-align: center;
  padding: 2rem;
}

h1 {
  color: #2c3e50;
}

p {
  font-size: 1.2rem;
  margin: 1rem 0 2rem;
  color: #34495e;
}

.actions {
  display: flex;
  justify-content: center;
  gap: 1.5rem;
}

.action-link {
  background-color: #3498db;
  color: white;
  text-decoration: none;
  padding: 0.75rem 1.5rem;
  border-radius: 5px;
  font-size: 1rem;
  font-weight: bold;
  transition: background-color 0.3s;
}

.action-link:hover {
  background-color: #2980b9;
}
</style>