// utils/urlChecker.js
export function containsCoolSite(url) {
    return url.includes('cool-site');
}

// utils/urlChecker.test.js
import { containsCoolSite } from './urlChecker';

describe('URL Checker Utility', () => {
    test('Returns true when the URL contains "cool-site"', () => {
        const url = 'https://www.example.com/cool-site';
        expect(containsCoolSite(url)).toBe(true);
    });

    test('Returns false when the URL does not contain "cool-site"', () => {
        const url = 'https://www.example.com/another-site';
        expect(containsCoolSite(url)).toBe(false);
    });

    test('Returns false when the URL is empty', () => {
        const url = '';
        expect(containsCoolSite(url)).toBe(false);
    });

    test('Returns false when the URL is null', () => {
        const url = null;
        expect(containsCoolSite(url)).toBe(false);
    });

    test('Returns false when the URL is undefined', () => {
        const url = undefined;
        expect(containsCoolSite(url)).toBe(false);
    });
});