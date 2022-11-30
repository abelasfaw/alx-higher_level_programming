#!/usr/bin/node
function compareNumbers (a, b) {
  return a - b;
}
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  args.forEach((element, index) => {
    args[index] = parseInt(element);
  });
  console.log(args.sort(compareNumbers)[args.length - 2]);
}
