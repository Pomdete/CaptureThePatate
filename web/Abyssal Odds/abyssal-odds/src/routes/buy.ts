import { renderTemplate } from "../templates";

const PRICE = 125;

export default eventHandler(async (event) => {
  let error = "";
  const hasEnoughCoins = event.session.coins >= PRICE;

  if (event.method === "POST") {
    if (event.session.coins >= PRICE) {
      event.session.coins -= PRICE;
      const box = createBox();
      event.session.boxes.set(box.id, box);

      return renderTemplate(event, "buy", {
        error,
        box,
        price: PRICE,
        hasEnoughCoins,
      });
    }

    error = "Not enough coins";
  }

  return renderTemplate(event, "buy", {
    error,
    price: PRICE,
    hasEnoughCoins,
  });
});
