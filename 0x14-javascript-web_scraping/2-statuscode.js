#!/usr/bin/node
// displays the status code of a GET request.

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log('error:', error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
