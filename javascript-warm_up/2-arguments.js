#!/usr/bin/node
const argumentVector = process.argv.slice(2);
const scrii = argumentVector.length <= 1 ? (argumentVector.length === 1 ? 'Argument found' : 'No argument') : 'Arguments found';
console.log(scrii);
