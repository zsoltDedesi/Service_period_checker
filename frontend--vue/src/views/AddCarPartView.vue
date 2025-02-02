<template>
    <div>
        <h1>Add Car Part</h1>
            <form @submit.prevent="submitForm" class="form-container">
                <label>Car Name:</label>
                <input v-model="carPart.car_name" required />

                <label>Part Name:</label>
                <input v-model="carPart.part_name" required />

                <label>Interval (km):</label>
                <input type="number" v-model="carPart.interval" required />

                <label>Last Replacement:</label>
                <input type="date" v-model="carPart.last_replacement" required />

                <label>Notes:</label>
                <textarea v-model="carPart.notes"></textarea>

                <button v-on:click="submitForm" type="submit">Submit</button>
            </form>
    </div>
</template>

<script>
import { addCarPart } from "@/api/carParts";

export default {
    name: "AddCarPartsView",
    data() {
        return {
            carPart: {
                car_name: "",
                part_name: "",
                interval: 0,
                last_replacement: "",
                notes: "",
            },
        };
    },
    methods: {
        async submitForm() {
            console.log(this.carPart);
            
            // await addCarPart(this.carPart);
            alert("Car part added successfully!");
            this.resetForm();
        },
        resetForm() {
            this.carPart = {
                car_name: "",
                part_name: "",
                interval: 0,
                last_replacement: "",
                notes: "",
            };
        },
    },
};
</script>

<style scoped>

.form-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 10px;
}

input, textarea{
    height: 30px;
    width: 30%;
}

textarea {
    height: 100px;
}

button {
    margin-top: 2rem;
}

label {
    text-align: left;
}

</style>
