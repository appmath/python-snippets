function generateRandomEmail() {
    const domains = ["example.com", "test.com", "sample.org"];
    const usernameLength = Math.floor(Math.random() * (12 - 6 + 1)) + 6;
    const username = Array.from({ length: usernameLength }, () =>
        String.fromCharCode(Math.floor(Math.random() * 36) + (Math.random() < 0.5 ? 48 : 87))
    ).join('');
    const domain = domains[Math.floor(Math.random() * domains.length)];
    return `${username}@${domain}`;
}

// Generate a random email address
const randomEmail = generateRandomEmail();
console.log(randomEmail);