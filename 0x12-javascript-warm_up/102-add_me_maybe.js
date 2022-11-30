#!/usr/bin/node
exports.addMeMaybe = function (arg, callback) {
  const newArg = arg + 1;
  callback(newArg);
};
