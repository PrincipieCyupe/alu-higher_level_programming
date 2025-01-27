#!/usr/bin/node
const argv = process.argv.slice(2);
const newv = argv[0] ? argv[0] : 'No argument';
console.log(newv);
