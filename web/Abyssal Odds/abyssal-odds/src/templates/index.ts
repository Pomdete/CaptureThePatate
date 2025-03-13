import { H3Event } from "h3";
import layout from "./_layout.hbs";
import about from "./about.hbs";
import collection from "./collection.hbs";
import buy from "./buy.hbs";
import open from "./open.hbs";
import index from "./index.hbs";

const templates = {
  about,
  collection,
  buy,
  open,
  index,
} as const;

export function renderTemplate(
  event: H3Event,
  template: keyof typeof templates,
  data: Record<string, unknown> = {}
) {
  return templates[template](
    { ...data, event },
    {
      partials: { layout },
    }
  );
}
