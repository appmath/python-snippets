import random
import string


def generate_password(length=20):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters to ensure complexity requirements.")

    # Define the character sets
    special_chars = "!@#$%^&*()-_=+"
    alphabet = string.ascii_letters  # Contains both lowercase and uppercase letters
    digits = string.digits

    # Ensure the password contains at least one character from each category
    password_chars = [
        random.choice(special_chars),
        random.choice(alphabet),
        random.choice(digits),
    ]

    # Fill the rest of the password length with a mix of all characters
    all_chars = special_chars + alphabet + digits
    password_chars.extend(random.choice(all_chars) for _ in range(length - len(password_chars)))

    # Shuffle the list to ensure random distribution of characters
    random.shuffle(password_chars)

    # Join the list into a string to form the password
    password = ''.join(password_chars)
    return password


# Generate a random password
print(generate_password(20))
