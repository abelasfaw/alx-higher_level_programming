#!/usr/bin/node
if (!(isNaN(parseInt(process.argv[2])))) {
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
} else {
  console.log('Missing size');
}
