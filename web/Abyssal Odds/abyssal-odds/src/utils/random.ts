export function randomNumber() {
  return Math.floor(Math.random() * 0xffffffff);
}

export function randomStr() {
  return randomNumber().toString(36);
}

export function randomHex() {
  return (
    randomNumber().toString(16).padStart(8, "0") +
    randomNumber().toString(16).padStart(8, "0")
  );
}
