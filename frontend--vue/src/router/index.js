// export default router;

// import { createRouter, createWebHistory } from "vue-router";
// import HomePage from "@/views/HomePage.vue";
// import CarPartsPage from "@/views/CarPartsPage.vue";
// import AddCarPartPage from "@/views/AddCarPartPage.vue";

// const routes = [
//   { path: "/", name: "Home", component: HomePage },
//   { path: "/car-parts", name: "CarParts", component: CarPartsPage },
//   { path: "/add-car-part", name: "AddCarPart", component: AddCarPartPage },
// ];

// const router = createRouter({
//   history: createWebHistory(),
//   routes,
// });

// const router = createRouter({
//   history: createWebHistory(process.env.BASE_URL),
//   routes,
// });

import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("../views/HomePage.vue"),
  },
  {
    path: "/car-parts",
    name: "CarParts",
    component: () => import("../views/CarPartsView.vue"),
  },
  {
    path: "/add-car-part",
    name: "AddCarParts",
    component: () => import("../views/AddCarPartView.vue")
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
