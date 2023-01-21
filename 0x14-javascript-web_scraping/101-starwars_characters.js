#!/usr/bin/node
// prints all characters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function print (characters) {
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], (error, response, body) => {
      if (error) {
        console.log(error);
      } else {
        console.log(JSON.parse(body).name);
      }
    });
  }
}
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    print(characters);
  }
});
