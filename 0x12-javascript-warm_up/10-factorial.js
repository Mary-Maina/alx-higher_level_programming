#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1;
  }
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg = process.argv[2];
const n = parseInt(arg);
console.log(factorial(n));
