#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    const char = c || 'X';
    if (this.width && this.height) {
      for (let i = 0; i < this.height; i++) {
        console.log(char.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
