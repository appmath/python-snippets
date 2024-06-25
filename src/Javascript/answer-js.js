// utils/conversion.test.js
import { convertToAbbreviation } from './conversion';

describe('ConversionUtil', () => {
    test('Gets the correct key for text', () => {
        const result = convertToAbbreviation('text');
        expect(result).toBe('txt');
    });

    test('Gets the correct key for email', () => {
        const result = convertToAbbreviation('email');
        expect(result).toBe('em');
    });

    test('Returns null for an unknown key', () => {
        const result = convertToAbbreviation('unknown');
        expect(result).toBeNull();
    });

    test('Returns null when input is null', () => {
        const result = convertToAbbreviation(null);
        expect(result).toBeNull();
    });

    test('Returns null when input is undefined', () => {
        const result = convertToAbbreviation(undefined);
        expect(result).toBeNull();
    });

    test('Returns null for an empty string', () => {
        const result = convertToAbbreviation('');
        expect(result).toBeNull();
    });
});