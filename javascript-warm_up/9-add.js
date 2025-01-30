#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const argv = process.argv.slice(2);
const num1 = parseInt(argv[0]);
const num2 = parseInt(argv[1]);
add(num1, num2);
