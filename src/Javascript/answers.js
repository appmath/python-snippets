// Define the arrow function and export it
export const generateCustomID = () => {
    const prefix = '00ud7t';
    const suffix = '1d7';
    const middleLength = 10; // The length of the middle part of the ID
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let middlePart = '';
    for (let i = 0; i < middleLength; i++) {
        middlePart += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    const fullID = prefix + middlePart + suffix;
    // Ensure the output is a JSON-valid string
    return JSON.stringify(fullID);
};

// Example usage in another file (assuming this file is named 'idGenerator.js')
// import { generateCustomID } from './idGenerator';
// console.log(generateCustomID());


