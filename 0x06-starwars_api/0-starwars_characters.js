#!/usr/bin/env node

const request = require('request');

// Function to get Star Wars characters by movie ID
function getStarWarsCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;

    request(url, (error, response, body) => {
        if (error || response.statusCode !== 200) {
            console.error("Movie not found or an error occurred.");
            return;
        }

        const movieData = JSON.parse(body);
        const characters = movieData.characters;

        // Fetch character names
        characters.forEach(characterUrl => {
            request(characterUrl, (error, response, body) => {
                if (!error && response.statusCode === 200) {
                    const characterData = JSON.parse(body);
                    console.log(characterData.name);
                }
            });
        });
    });
}

// Main execution
const movieId = process.argv[2];

if (!movieId) {
    console.log("Usage: ./0-starwars_characters.js <movie_id>");
    process.exit(1);
}

getStarWarsCharacters(movieId);
