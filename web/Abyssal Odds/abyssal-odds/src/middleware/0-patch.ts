// Patch the app, someone managed to get all the cards from the deck
// I don't know how they did it, but I'm sure it's related to the random number generator
// With this patch, it should be impossible to predict the next number
// I hope this is enough to fix the issue
export default defineEventHandler((event) => {
  const rounds = Math.floor(Math.random() * 100);

  for (let i = 0; i < rounds; i++) {
    Math.random();
  }
});
