#!/usr/bin/node
// adds two arguments
function add (a, b) {
  return a + b;
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

if (isNaN(parseInt(arg1)) || isNaN(parseInt(arg2))) {
  console.log('Missing or invalid arguments');
} else {
  const num1 = parseInt(arg1);
  const num2 = parseInt(arg2);
  console.log(add(num1, num2));
}
