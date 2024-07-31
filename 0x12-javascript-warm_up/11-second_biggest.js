#!/usr/bin/node
// checks the second biggest argument

const args = process.argv.slice(2);
if (args.length < 2) {
  console.log(0);
} else {
  const numbers = args.map(Number);
  numbers.sort((a, b) => b - a);
  const secondBiggest = numbers[1];
  console.log(secondBiggest);
}
