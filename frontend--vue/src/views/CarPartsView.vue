<template>
  <div class="car-parts-view">
    <h1>Car Parts List</h1>
    <p v-if="loading">Loading car parts...</p>
    <p v-if="error" class="error-message">{{ error }}</p>
    <div class="popup-button-container">
      <button @click="addNewItemPopup" class="popup">Add new car</button>
    </div>
    <AddCarPartPopup 
      v-if="popupVisible" 
      :data="selectedCarPart" 
      :isSave="isSaveMode" 
      @save="handleSave"
      @close="popupVisible = false" />
      
    <div class="table-container">
      <table v-if="carParts.length > 0" class="car-parts-table">
        <thead>
          <tr>
            <!-- <th>ID</th> -->
            <th>Car Name</th>
            <th>Part Name</th>
            <th>Interval</th>
            <th>Last Replacement</th>
            <th>Notes</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="part in carParts" :key="part.id">
            <!-- <td>{{ part.id }}</td> -->
            <td>{{ part.car_name }}</td>
            <td>{{ part.part_name }}</td>
            <td>{{ part.interval }}</td>
            <td>{{ part.last_replacement }}</td>
            <td>{{ part.notes }}</td>
            <td class="button-col">
              <div class="button-container">
                <button @click="modifyItemPopup(part)">Modify</button>
                <button @click="deleteItem(part.id)" class="delete-button">Delete</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
      <p v-else>No car parts available.</p>
    </div>
  </div>
</template>

<script>
import { addCarPart, getCarParts, deleteCarPart, modifyCarPart } from "@/api/carParts";
import AddCarPartPopup from "../components/AddCarPartPopup.vue";

export default {
  components: { AddCarPartPopup },
  name: "CarPartsView",
  data() {
    return {
      carParts: [],
      loading: true,
      error: null,
      selectedCarPart: null,
      popupVisible: false,
      isSaveMode: false,
    };
  },
  methods: {
    async fetchItem() {
      try {
        const response = await getCarParts()
        if (response) {
          console.log("Car parts has been listed");
          this.carParts = response
        }
      } catch (err) {
        this.error = "Failed to load car parts. Please try again later.";
        console.log(this.error);
      } finally {
        this.loading = false;
      }
    },

    async deleteItem(id) {
      try {
        console.log(`Selected id: ${id}`)
        const response = await deleteCarPart(id);
        if (response) {
          console.log(response.message);
          this.carParts = this.carParts.filter((part) => part.id !== id);
        }
      } catch (error) {
        console.error("Error during delete method:", error);
      }
    },

    async addItem(data) {
      try {
        console.log(`This is a data from popup: ${data}`)
        const response = await addCarPart(data);
        console.log("Response:", response.message);
      } catch (error) {
        console.error("Error submitting form:", error);
      }
    },

    async modifyItem(data) {
      try {
        const response = await modifyCarPart(data.id, data);
        console.log("Response:", response.message);
      } catch (error) {
        console.error("Error modify form:", error);
      }
    },

    addNewItemPopup() {
      this.selectedCarPart = { car_name: "", part_name: "", interval: "", last_replacement: "", notes: "" };
      this.popupVisible = true,
      this.isSaveMode = true
    },

    modifyItemPopup(part) {
      this.selectedCarPart = { ...part };
      this.popupVisible = true,
        this.isSaveMode = false
    },

    async handleSave(updatedPart) {
      if (this.isSaveMode) {
        // add new object
        this.carParts.push(updatedPart);
        this.addItem(updatedPart)

      } else {
        // update existing object
        const index = this.carParts.findIndex((part) => part.id === updatedPart.id);
        if (index !== -1) {
          this.carParts.splice(index, 1, updatedPart);
          this.modifyItem(updatedPart)
        }
      }
      this.popupVisible = false;
    }
  },

  created() {
    this.fetchItem();
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

table {
  color: black;
  border: 1px solid hsl(0, 0%, 10%);
  background-color: #cacaca;
}

.table-container {
  width: 80%;
  margin: 0 auto;
  height: calc(100vh - 400px);
  overflow-y: auto;
}

.car-parts-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
}

.car-parts-table thead {
  position: sticky;
  top: -0.1px;
  z-index: 5;
  height: 3rem;
  line-height: 3rem;

}

.car-parts-table th,
.car-parts-table td {
  padding: 0.5rem;
}

.car-parts-table th {
  background-color: hsl(0, 0%, 50%);
  font-weight: bold;
}

.car-parts-table tr {
  border: 1px solid hsl(0, 0%, 10%);
}


.car-parts-table tr:hover {
  background-color: hsl(0, 0%, 60%);
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 1rem;
}

.button-container {
  display: flex;
  gap: 15px;
  justify-content: center;
  align-content: stretch;
}

.button-col {
  max-width: 80px;
}

.popup-button-container {
  max-width: 80%;
  display: flex;
  margin: auto;

  justify-content: end;
  align-items: center;
  /* margin: 0 10rem 0 10rem; */
}

.popup {
  margin: 2rem;
}

.delete-button:hover {
  background-color: hsl(0, 60%, 40%);
  border: 1px solid hsl(0, 60%, 30%);;
}


</style>