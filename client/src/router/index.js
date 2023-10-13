import { createRouter, createWebHistory } from "vue-router";
import home from "../views/HomeView.vue";
import portBot from "../views/PortBotView.vue";
import portConnections from "../views/PortConnections.vue";
import SkillsReportingView from "../views/SkillsReportingView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: home,
    },
    {
      path: "/portbot",
      name: "portBot",
      component: portBot,
    },
    {
      path: "/portconnections",
      name: "port",
      component: portConnections,
    },
    {
      path: "/lighthouse",
      name: "SkillsReportingView",
      component: SkillsReportingView,
    },
  ],
});

export default router;
