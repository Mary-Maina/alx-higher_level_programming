#!/usr/bin/node
/* This is an argument
 * that prints the first argument
 */
const args = process.argv.slice(2);
const first = args[0];
if (first === undefined) {
  console.log('No argument');
} else {
  console.log(first);
}
