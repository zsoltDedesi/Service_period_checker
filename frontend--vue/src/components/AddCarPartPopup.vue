<template>
  <div class="modal-overlay">
    <div class="modal">
      <div class="modal-body">

        <div class="input-box-container">
          <label>Car Name:</label>
          <input v-model="inputData.car_name" required />
        </div>

        <div class="input-box-container">
          <label>Part Name:</label>
          <input v-model="inputData.part_name" required />
        </div>

        <div class="input-box-container">
          <label>Interval (km):</label>
          <input type="number" v-model="inputData.interval" required />
        </div>

        <div class="input-box-container">
          <label>Last Replacement:</label>
          <input type="date" v-model="inputData.last_replacement" required />
        </div>

        <div class="input-box-container">
          <label>Notes:</label>
          <textarea v-model="inputData.notes"></textarea>
        </div>

      </div>
        <!-- <button v-on:click="submitForm" type="submit" :disabled="isSubmitting">Submit</button> -->
      <div class="button-container">
        <button @click="closePopup" class="cancel">Cancel</button>
        <button v-if="isSave" @click="saveData" class="save">Save</button>
        <button v-else @click="saveData" class="save">Modify</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    data: Object,
    isSave: Boolean
  },

  data() {
    return {
      inputData: { ...this.data }
    };
  },

  methods: {
    saveData() {
      this.$emit("save", { ...this.inputData });
    },
    closePopup() {
      this.$emit("close"); //event emit to parent component
    },
  },
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
}

.modal {
  background: hsl(0, 0%, 35%);
  width: 20%;
  /* height: 50%; */
  padding: 3em;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: end;
  /* align-items: center; */
}

/* .modal-body {
  /* display: flex; */
/* flex-direction: column; */
/* justify-content: space-evenly; */
/* margin: auto;
} */

.input-box-container {
  display: flex;
  flex-direction: column;
  /* justify-content: center; */
  /* align-items: start; */
  /* justify-content: space-evenly; */
  margin: 1em;
}

input {
  height: 2em;
  width: auto;
  /* width:  20rem; */
  /* width: 100%; */
  font-size: 1rem;
  padding-left: 20px;
}

input[type="date"] {
  height: 2.5em;
  width: auto;
  text-align: start;
  font-size: 1rem;
  padding-left: 20px;
}

label {
  text-align: start;
}

textarea {
  min-height: 5em;
  width: auto;
  font-size: 1rem;
  padding-left: 20px;
  resize: vertical;
}

.button-container {
  display: flex;
  gap: 2rem;
  justify-content: center;
  align-items: center;
  /* align-content: stretch; */
  flex-direction: row;

}

button {
  width: 10em;
  height: 3em;
  text-align: center;
  margin-top: 3em;
}
</style>
