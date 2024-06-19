#!/usr/bin/node
/* script that prints an argument
 * if it is an integer or can be converted to an int
 */
const args = process.argv[2];
if (!isNaN(Number(args))) {
  console.log('My number:', parseInt(args, 10));
} else {
  console.log('Not a number');
}
