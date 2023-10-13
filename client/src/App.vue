<script setup>
import SideNavbar from './components/SideNavbar.vue';
</script>

<template>

  <div class="app">
    <SideNavbar/>
    <RouterView />
  </div>
  
</template>

<style lang="scss">
:root {
    --primary: #7cbeb6;
    --secondary: #0582ca;
    --tertiary: #fcbf01;
    --dark: #08090a;
    --grey: #dbd3d8;
    --light: #faf9f6;
    --sidenavbar-width: 300px;
    --root-em: 18px;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Poppins', sans-serif;
}

body {
    background-color: white;
}

button {
    border: none;
    outline: none;
    appearance: none;
    background-color: transparent;
    cursor: pointer;
}

.app {
    display: flex;

    main {
        flex: 1 1 0;
        padding: 2rem;

        @media (max-width: 768px) {
            padding: 1rem;
        }
    }
}
</style>
