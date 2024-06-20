#!/usr/bin/node
// prints C is fun x times
const x = process.argv[2];

if (!isNaN(Number(x)) && parseInt(x, 10) > 0) {
  for (let i = 0; i < parseInt(x, 10); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
