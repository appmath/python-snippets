function generateRandomPassword(length) {
    // Define character sets
    const uppercaseChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const lowercaseChars = 'abcdefghijklmnopqrstuvwxyz';
    const numberChars = '0123456789';
    const symbolChars = '!@#$%^&*()_+-=[]{}|;:\'",.<>?/~`';

    // Combine all character sets
    const allChars = uppercaseChars + lowercaseChars + numberChars + symbolChars;

    // Ensure the password includes at least one character from each set
    const passwordArray = [
        uppercaseChars[Math.floor(Math.random() * uppercaseChars.length)],
        lowercaseChars[Math.floor(Math.random() * lowercaseChars.length)],
        numberChars[Math.floor(Math.random() * numberChars.length)],
        symbolChars[Math.floor(Math.random() * symbolChars.length)]
    ];

    // Fill the rest of the password length with random characters from all sets
    for (let i = passwordArray.length; i < length; i++) {
        passwordArray.push(allChars[Math.floor(Math.random() * allChars.length)]);
    }

    // Shuffle the array to ensure randomness of character distribution
    for (let i = passwordArray.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [passwordArray[i], passwordArray[j]] = [passwordArray[j], passwordArray[i]]; // ES6 array destructuring swap
    }

    return passwordArray;
}

// Example usage:
const passwordLength = 12; // You can change this to any desired length
const randomPasswordArray = generateRandomPassword(passwordLength);
console.log(randomPasswordArray);
