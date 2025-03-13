export const fullCollection = [
  { name: "Ocean Pearl Bivalve", img: "/mussle.webp" },
  { name: "Royal Crustacean", img: "/crab.webp" },
  { name: "Luminescent Medusa", img: "/jellyfish.webp" },
  { name: "Sovereign Cephalopod", img: "/octopus.webp" },
  { name: "Coral Reef Specter", img: "/shrimp.webp" },
  { name: "Celestial Seastar", img: "/star.webp" },
  { name: "Majestic Chelonian", img: "/turtle.webp" },
  { name: "Treasure Trove", img: "/molluscs.webp" },
] as const;

export interface LootBox {
  id: string;
  seed: number;
}

export function createBox() {
  return {
    id: randomHex(),
    seed: randomNumber(),
  };
}

function _openBox(box: LootBox, key: number) {
  const ts = Math.floor(Date.now() / 1000);
  switch (true) {
    case key === box.seed:
      return 1;
    case Math.abs(key - ts) < 60:
      return 2;
    case box.seed % key === 0:
      return 3;
    case Math.cos(key) * 0 !== 0:
      return 4;
    case key && (box.seed * key) % 1337 === 0:
      return 5;
    case key && (box.seed | key) === (box.seed | 0):
      return 6;
    case !(key < 0) && box.seed / key < 0:
      return 7;
    default:
      return 0;
  }
}

export function openBox(box: LootBox, key: number) {
  const lootId = _openBox(box, key);
  const loot = fullCollection[lootId];
  console.log(`[BOX OPEN] seed=${box.seed} key=${key} result=${loot.name}`);
  return { loot, lootId };
}
