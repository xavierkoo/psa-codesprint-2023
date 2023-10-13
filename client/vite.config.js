import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  server: {
    host: true, // enable routing from external (webpage served to user) to intenal container (docker container with the vue)
    port: 8080,
    proxy: {
      "/api/safe": {
        // auto appends to the target
        target: "http://server_backend:5101", // URL of Container 2
        changeOrigin: true,
        secure: false, // Insecure, but okay for local development
      },
      "/generate_chat": {
        // auto appends to the target
        target: "http://server_backend:5101", // URL of Container 2
        changeOrigin: true,
        secure: false, // Insecure, but okay for local development
      },
    },
  },
});
