#!/usr/bin/node
const argv = process.argv.slice(2);
const txt = parseInt(argv[0]);
const str = 'C is fun';
if (isNaN(txt)) {
  console.log('Missing number of occurrences');
} else {
  let i = 0; while (i < txt) { console.log(str); i++; }
}
