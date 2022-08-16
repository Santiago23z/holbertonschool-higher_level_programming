#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.heigth = h;
    }
  }

  print () {
    for (let index = 0; index < this.heigth; index++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const tmp = this.width;
    this.width = this.heigth;
    this.heigth = tmp;
  }

  double () {
    this.heigth *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
