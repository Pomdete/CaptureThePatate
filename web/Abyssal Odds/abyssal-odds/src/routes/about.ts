import { renderTemplate } from "../templates";

export default eventHandler((event) => {
  return renderTemplate(event, "about");
});
