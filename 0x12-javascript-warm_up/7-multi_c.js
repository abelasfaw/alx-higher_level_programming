#!/usr/bin/node
if (!(isNaN(parseInt(process.argv[2])))) {
  const loops = parseInt(process.argv[2]);
  for (let i = 0; i < loops; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
