const priceRose = 8;
let numRose = 70;
const priceLily = 10;
let numLily = 50;
const priceTulip = 2;
let numTulip = 120;

let totalRose = priceRose * numRose;
let totalLily = priceLily * numLily;
let totalTulip = priceTulip * numTulip;

let total = totalRose + totalLily + totalTulip;

console.log("Rose - unit price:", priceRose, ", quantity:", numRose, ", value:", totalRose);
console.log("Lily - unit price:", priceLily, ", quantity:", numLily, ", value:", totalLily);
console.log("Tulip - unit price:", priceTulip, ", quantity:", numTulip, ", value:", totalTulip);
console.log(total);

numRose -= 20;
numLily -= 30;

totalRose = priceRose * numRose;
totalLily = priceLily * numLily;
totalTulip = priceTulip * numTulip;

total = totalRose + totalLily + totalTulip;

console.log("Rose - unit price:", priceRose, ", quantity:", numRose, ", value:", totalRose);
console.log("Lily - unit price:", priceLily, ", quantity:", numLily, ", value:", totalLily);
console.log("Tulip - unit price:", priceTulip, ", quantity:", numTulip, ", value:", totalTulip);
console.log(total);