#!/usr/bin/node
exports.esrever = function (list) {
  if (list.length >= 1) {
    for (let i = 0; i < (list.length / 2); i++) {
      const leftElement = list[i];
      list[i] = list[list.length - 1 - i];
      list[list.length - 1 - i] = leftElement;
    }
  }
  return list;
};
