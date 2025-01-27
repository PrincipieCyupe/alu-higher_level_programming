#!/usr/bin/node
const argument_vector = process.argv.slice(2);
const scrii = argument_vector.length <= 1 ? (argument_vector.length === 1 ? 'Argument found' : 'No argument') : 'Arguments found';
console.log(scrii);
