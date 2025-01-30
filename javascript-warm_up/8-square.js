#!/usr/bin/node
const argv = process.argv.slice(2);
const txt = parseInt(argv[0]);
if (!isNaN(txt)) {
  for (let i = 0; i < txt; i++) { console.log('X'.repeat(txt)); }
} else {
  console.log('Missing size');
}
