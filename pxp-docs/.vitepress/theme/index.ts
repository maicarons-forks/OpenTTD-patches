import DefaultTheme from "vitepress/theme";
import DocFigure from "./components/DocFigure.vue";
import "./style.css";

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component("DocFigure", DocFigure);
  },
};
