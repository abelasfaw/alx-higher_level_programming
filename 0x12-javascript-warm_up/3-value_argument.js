#!/usr/bin/node
let printed = false;
process.argv.forEach((value, index) => {
  if (index === 2) {
    console.log(value);
    printed = true;
  }
});
if (!printed) {
  console.log('No argument');
}
