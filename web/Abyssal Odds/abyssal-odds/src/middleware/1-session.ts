import { type LootBox } from "../utils/collection";

declare module "h3" {
  interface H3Event {
    session: Session;
    nonce: string;
    csrfToken: string;
  }
}

const COOKIE_NAME = "session_id";

interface Session {
  id: string;
  coins: number;
  collection: Set<number>;
  boxes: Map<string, LootBox>;
}

const sessions = new Map<string, Session>();

export default defineEventHandler((event) => {
  let sessionId = getCookie(event, COOKIE_NAME);
  if (!sessionId) {
    sessionId = randomHex();
    setCookie(event, COOKIE_NAME, sessionId);
  }

  let session = sessions.get(sessionId);
  if (!session) {
    session = {
      id: sessionId,
      coins: 1000,
      collection: new Set(),
      boxes: new Map(),
    };
    sessions.set(sessionId, session);
  }
  event.session = session;

  // CSP stuff
  event.nonce = randomHex();
  setHeader(
    event,
    "Content-Security-Policy",
    `default-src 'self'; style-src 'unsafe-inline'; script-src 'nonce-${event.nonce}'  https://cdn.tailwindcss.com/  ; img-src *`
  );

  // CSRF stuff

  let cookieToken = getCookie(event, "csrf_token");
  if (!cookieToken) {
    cookieToken = randomHex();
    setCookie(event, "csrf_token", cookieToken);
  }
  event.csrfToken = cookieToken;
});
