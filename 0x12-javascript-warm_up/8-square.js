#!/usr/bin/node
// Get the first command-line argument as the size of the square
const size = process.argv[2];
if (isNaN(parseInt(size))) {
  console.log('Missing size');
} else {
  const n = parseInt(size);
  for (let i = 0; i < n; i++) {
    let row = '';
    for (let j = 0; j < n; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
