#!/usr/bin/node
/* script that prints an argument
 * if it is an integer or can be converted to an int
 */
const args = process.argv.slice(2);
const first = args[0];
const number = parseInt(first, 10);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My Number: ' + number);
}
