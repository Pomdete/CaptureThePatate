//https://nitro.unjs.io/config
import { extname } from "upath";

export default defineNitroConfig({
  rollupConfig: {
    plugins: [
      {
        name: "handlebars-loader",
        transform(code: string, id: string) {
          if (id[0] !== "\0" && extname(id) === ".hbs") {
            const result = `// ${id}
  import Handlebars from "handlebars";
  export default Handlebars.compile(${JSON.stringify(code)});
  `;
            return {code: result, map: null};
          }
        },
      },
    ],
  },
});
