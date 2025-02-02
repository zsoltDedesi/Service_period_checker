import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:5000/api", // Flask backend URL
  headers: {
    "Content-Type": "application/json",
  },
});

// GET - Autóalkatrészek lekérése
export const getCarParts = async () => {
  const response = await apiClient.get("/data/car-parts");
  return response.data;
};

// POST - Új alkatrész hozzáadása
export const addCarPart = async (part) => {
  const response = await apiClient.post("/data/car-parts", part);
  return response.data;
};
