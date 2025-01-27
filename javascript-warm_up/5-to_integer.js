#!/usr/bin/node
const argv = process.argv.slice(2);
const textfile = 'My number:';
const message = parseInt(argv[0]) ? `${textfile} ${parseInt(argv[0])}` : 'Not a number';
console.log(message);
