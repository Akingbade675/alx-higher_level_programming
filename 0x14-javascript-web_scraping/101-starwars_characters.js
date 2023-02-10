#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, async (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const { characters } = JSON.parse(body);

    for (const character of characters) {
      console.log(character);
      await request(character, (err, res, body) => {
        if (err) {
          console.log(err);
          return;
        }
        const { name } = JSON.parse(body);
        console.log(name);
      });
    }
  }
});
