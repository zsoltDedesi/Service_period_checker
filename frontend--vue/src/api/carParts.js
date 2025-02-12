import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://127.0.0.1:5000/api", // Flask backend URL
  headers: {
    "Content-Type": "application/json",
  },
});

export const getCarParts = async () => {
  const response = await apiClient.get("/data/car-parts");
  return response.data;
};

export const addCarPart = async (part) => {
  const response = await apiClient.post("/data/car-parts", part);
  return response.data;
};

export const deleteCarPart = async (id) => {
  const response = await apiClient.delete(`/data/car-parts/${id}`);
  return response.data;
};

export const modifyCarPart = async (id, part) => {
  const response = await apiClient.patch(`/data/car-parts/${id}`, part);
  return response.data;
};
