#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err); // Print errors exactly as expected
    return;
  }
  process.stdout.write(data); // Avoid extra newlines
});
