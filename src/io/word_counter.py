def count_word_in_file(file_path, word_to_count):
    try:
        # Open the file
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the contents
            content = file.read()

            # Convert content to lower case for case-insensitive counting
            content = content.lower()

            # Convert the word to lower case
            word_to_count = word_to_count.lower()

            # Count the occurrences
            count = content.count(word_to_count)

            return count

    except FileNotFoundError:
        print("File not found.")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0


# Example usage
file_path = 'path/to/your/file.txt'
word = 'example'
frequency = count_word_in_file(file_path, word)
print(f"The word '{word}' appears {frequency} times in the file.")
