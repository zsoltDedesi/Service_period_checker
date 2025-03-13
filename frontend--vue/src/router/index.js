
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
