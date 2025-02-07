#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err); // Use console.error for error messages
    return;
  }
  process.stdout.write(data); // Use process.stdout.write to avoid extra new lines
});
