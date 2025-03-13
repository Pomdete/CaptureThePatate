import { H3Event, readBody } from "h3";
import { z } from "zod";

export async function useBody<T extends z.ZodTypeAny>(
  event: H3Event,
  parser: T
) {
  const body = await readBody(event);


  if (body?.csrf_token !== event.csrfToken) {
    throw createError({
      statusCode: 403,
      message: "Invalid CSRF token",
    });
  }
  return parser.parse(body);
}
