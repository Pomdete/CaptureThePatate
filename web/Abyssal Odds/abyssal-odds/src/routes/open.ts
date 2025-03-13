import { z } from "zod";
import { useBody } from "../utils/useBody";
import { renderTemplate } from "../templates";

export default defineEventHandler(async (event) => {
  if (event.method !== "POST") {
    throw createError({
      statusCode: 405,
      message: "Method not allowed",
    });
  }

  const { key, boxId } = await useBody(
    event,
    z.object({
      action: z.literal("open"),
      key: z.coerce.number().transform((r) => Math.trunc(r)),
      boxId: z.string(),
    })
  );

  const box = event.session.boxes.get(boxId);
  if (!box) {
    throw createError({
      statusCode: 404,
      message: "Box not found",
    });
  }

  const { loot, lootId } = openBox(box, key);
  event.session.collection.add(lootId);
  event.session.boxes.delete(boxId);

  return renderTemplate(event, "open", {
    lootId,
    loot,
  });
});
