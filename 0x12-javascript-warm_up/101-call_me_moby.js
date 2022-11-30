#!/usr/bin/node
exports.callMeMoby = function (iteration, callback) {
  for (let i = 0; i < iteration; i++) {
    callback();
  }
};
