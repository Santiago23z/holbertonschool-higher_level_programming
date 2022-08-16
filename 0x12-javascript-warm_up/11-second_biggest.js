#!/usr/bin/node

const len = process.argv.length;
const num = process.argv.slice(2).map(function (n) {
  return parseInt(n);
});
const max = Math.max.apply(Math, num);
const min = Math.min.apply(Math, num);

if (len > 3) {
  let i = 0;
  let n = 0;
  let secBig = min;

  for (; i < len; ++i) {
    n = num[i];

    if (n > secBig && n < max) {
      secBig = n;
    }
  }

  console.log(secBig);
} else {
  console.log(0);
}
