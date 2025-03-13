<template>
  <div id="app">
    <header>
      <nav>
        <ul>
          <li><router-link to="/">Home</router-link></li>
          <li><router-link to="/car-parts">Car Parts</router-link></li>
          <li><router-link to="/add-car-part">Add Car Part</router-link></li>
        </ul>
      </nav>
    </header>
    <main>
      <router-view />
    </main>
    <footer>
      <p>© 2025 Service Manager</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
/* Globális stílusok */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

header {
  background-color: #333;
  color: white;
  /* width: 100%; */
  padding: 1rem;
}

header ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

header li {
  margin-right: 1rem;
}

header a {
  color: white;
  text-decoration: none;
}

header a.router-link-active {
  font-weight: bold;
  text-decoration: underline;
}

/* main {
  padding: 2rem;
} */

footer {
  text-align: center;
  background-color: #333;
  color: white;
  /* padding: 1rem 0; */
  position: fixed;
  bottom: 0;
  width: 100%;
}
</style>
