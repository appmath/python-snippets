function generateRandomOktaId() {
        const prefix = '00ud7t';
        const suffix = '1d7';
        const middleLength = 10; // Total length is 20 - prefix (6) - suffix (3) = 11
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        let middlePart = '';
        for (let i = 0; i < middleLength; i++) {
            middlePart += characters.charAt(Math.floor(Math.random() * characters.length));
        }
        return prefix + middlePart + suffix;
    }
}


