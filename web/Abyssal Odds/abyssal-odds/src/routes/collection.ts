import { renderTemplate } from "../templates";

export default eventHandler((event) => {
  const collection = fullCollection.map((item, idx) => ({
    name: item.name,
    img: item.img,
    owned: event.session.collection.has(idx),
  }));

  const count = event.session.collection.size;
  const flag = count === fullCollection.length && (process.env.FLAG || "FCSC{flag}");
  return renderTemplate(event, "collection", { collection, flag });
});
