declare module "*.hbs" {
  import Handlebars from "handlebars";
  const template: Handlebars.TemplateDelegate;
  export default template;
}
