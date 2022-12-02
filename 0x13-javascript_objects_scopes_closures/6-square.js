#!/usr/bin/node
module.exports = class Sqaure extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let output = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          output += 'C';
        }
        console.log(output);
        output = '';
      }
    }
  }
};
