#!/usr/bin/node
// computes the number of tasks completed by user id.

const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const todos = JSON.parse(body);
    const result = {};
    for (let i = 0; i < todos.length; i++) {
      const status = (todos[i].completed);
      const key = todos[i].userId.toString();
      if (status) {
        if (result[key]) {
          result[key]++;
        } else {
          result[key] = 1;
        }
      }
    }
    console.log(result);
  }
});
