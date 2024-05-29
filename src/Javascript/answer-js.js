function generateRandomEmail(domainList = ["example.com", "test.com", "sample.org"], numEmails = 1) {
    const emails = [];

    for (let i = 0; i < numEmails; i++) {
        const usernameLength = Math.floor(Math.random() * (12 - 6 + 1)) + 6;
        const username = Array.from({ length: usernameLength }, () =>
            String.fromCharCode(Math.floor(Math.random() * 36) + (Math.random() < 0.5 ? 48 : 87))
        ).join('');
        const domain = domainList[Math.floor(Math.random() * domainList.length)];
        emails.push(`${username}@${domain}`);
    }

    return emails;
}

// Generate 10 random email addresses
const randomEmails = generateRandomEmail(undefined, 10);
randomEmails.forEach(email => console.log(email));