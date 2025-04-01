import axios from "axios";

const apiClient = axios.create({
  // baseURL: "http://192.168.1.17:5000/api", // Flask backend URL
  baseURL: "http://localhost:5000/api", // Flask backend URL
  headers: {
    "Content-Type": "application/json",
  },
});

export const getCarParts = async () => {
  const response = await apiClient.get("/data/car-parts");
  return response.data;
};

export const getCarPartById = async (id) => {
  const response = await apiClient.get(`/data/car-parts/${id}`);
  return response.data;
}

export const addCarPart = async (part) => {
  const response = await apiClient.post("/data/car-parts", part);
  return response.data;
};

export const deleteCarPart = async (id) => {
  const response = await apiClient.delete(`/data/car-parts/${id}`);
  return response.data;
};

export const modifyCarPart = async (id, part) => {
  const response = await apiClient.put(`/data/car-parts/${id}`, part);
  return response.data;
};
