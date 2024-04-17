function generateID() {
    const length = 12;
    const charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    const specialChars = "!@#$%^&*()_+-=[]{}|;:',.<>/?";
    let result = "";
    for (let i = 0; i < length - 1; i++) {
        result += charset.charAt(Math.floor(Math.random() * charset.length));
    }
    // Add a special character at a random position in the result
    const specialChar = specialChars.charAt(Math.floor(Math.random() * specialChars.length));
    const position = Math.floor(Math.random() * (result.length + 1));
    result = result.slice(0, position) + specialChar + result.slice(position);

    return result;
}

console.log(generateID());
