#!/usr/bin/node

const request = require('request');
const async = require('async');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('An error occurred while trying to retrieve the data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('An error occurred while trying to retrieve the data:', response.statusCode, response.statusMessage);
    return;
  }

  const movie = JSON.parse(body);
  async.eachSeries(movie.characters, (characterUrl, callback) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('An error occurred while trying to retrieve the data:', error);
        return callback(error);
      }

      if (response.statusCode !== 200) {
        console.error('An error occurred while trying to retrieve the data:', response.statusCode, response.statusMessage);
        return callback(new Error(response.statusMessage));
      }

      const character = JSON.parse(body);
      console.log(character.name);
      callback();
    });
  });
});
