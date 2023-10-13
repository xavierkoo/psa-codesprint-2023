<script setup>
import { ref } from 'vue'

const isMenuOpen = ref(false)

const toggleMenu = () => {
    isMenuOpen.value = !isMenuOpen.value
}
</script>

<template>
    <aside :class="`${isMenuOpen ? 'is-isMenuOpen' : ''}`">
        <div class="logo" :hidden="!isMenuOpen">
            <img src="../assets/logo.png" alt="logo_small" />
        </div>
        <div class="logo" :hidden="isMenuOpen">
            <img
                src="https://cdn.icon-icons.com/icons2/2699/PNG/512/docker_tile_logo_icon_168248.png"
                alt="brand_logo"
            />
        </div>

        <div class="menu-toggle-wrap">
            <button class="menu-toggle">
                <span class="material-icons" @click="toggleMenu"
                    >keyboard_double_arrow_right</span
                >
            </button>
        </div>

        <h3>Menu</h3>
        <div class="menu">
            <router-link class="button" to="/">
                <span class="material-icons">home</span>
                <span class="text">Home</span>
            </router-link>
            <router-link class="button" to="/portbot">
                <span class="material-icons">face</span>
                <span class="text">PortBot</span>
            </router-link>
            <router-link class="button" to="/lighthouse">
                <span class="material-icons">pageview</span>
                <span class="text">LightHouse</span>
            </router-link>
            <router-link class="button" to="/portconnections">
              <span class="material-icons">diversity_1</span>
              <span class="text">PortConnections</span>
          </router-link>
        </div>

        <div class="flex"></div>
        <div class="menu">
            <router-link class="button" to="/">
                <span class="material-icons">comment</span>
                <span class="text">Feedback</span>
            </router-link>
        </div>
    </aside>
</template>

<style lang="scss" scoped>
aside {
    display: flex;
    flex-direction: column;
    width: calc(2rem + 2rem);
    min-height: 100vh;
    overflow: hidden;
    padding: 1rem;

    color: var(--light);
    background-color: var(--dark);
    transition: 200ms ease-out;

    .flex {
        flex: 1 1 0;
    }

    .logo {
        margin-bottom: 1rem;
        img {
            width: 2rem;
        }
    }

    .menu-toggle-wrap {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 1rem;

        position: relative;
        top: 0;
        transition: 200ms ease-out;

        .menu-toggle {
            transition: 200ms ease-out;

            .material-icons {
                font-size: 2rem;
                color: (var(--light));
                transition: 200ms ease-out;
            }
            &:hover {
                .material-icons {
                    color: var(--primary);
                    transform: translateX(0.2rem);
                }
            }
        }
    }

    h3,
    .button .text {
        opacity: 0;
        transition: 300ms ease-out;
    }

    h3 {
        color: grey;
        font-size: 0.875rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
    }
    .menu {
        margin: 0 -1rem;

        .button {
            display: flex;
            align-items: center;
            text-decoration: none;

            padding: 0.5rem 1rem;
            transition: 300ms ease-out;

            .material-icons {
                font-size: 2rem;
                color: var(--light);
                transition: 200ms ease-out;
            }

            .text {
                color: var(--light);
                transition: 200ms ease-out;
            }

            &:hover,
            &.router-link-exact-active {
                background-color: var(--dark);
                .material-icons {
                    color: var(--primary);
                }
                .text {
                    color: var(--primary);
                }
            }

            &.router-link-exact-active {
                border-right: 5px solid var(--primary);
            }
        }
    }

    &.is-isMenuOpen {
        width: var(--sidenavbar-width);
        h3,
        .button .text {
            opacity: 1;
        }

        .logo {
            margin-bottom: 1rem;
            img {
                width: 10rem;
            }
        }

        .button {
            .material-icons {
                margin-right: 1rem;
            }
        }

        .menu-toggle-wrap {
            top: -3rem;
            .menu-toggle {
                .material-icons {
                    transform: rotate(180deg);
                }
            }
        }
    }

    @media (max-width: 768px) {
        position: fixed;
        z-index: 99;
    }
}
</style>
