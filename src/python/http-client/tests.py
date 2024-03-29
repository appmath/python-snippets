import re


def generate_script(input_file_path, output_file_path):
    # Regular expression to find the valueIds within the curly braces
    pattern = re.compile(r"const\s*\{([^}]+)\}\s*=\s*body;")

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()

        # Find the match using the regular expression
        match = pattern.search(content)
        if not match:
            print("No matching pattern found in the input file.")
            return

        # Extracting valueIds and removing whitespace
        value_ids = [value_id.strip() for value_id in match.group(1).split(',')]

        # Generating the output content
        output_lines = []
        for value_id in value_ids:
            output_lines.append(f'const ctic{value_id.capitalize()} = client.global.get("{value_id}");')
            output_lines.append(
                f'client.assert({value_id} === ctic{value_id.capitalize()}, `Expected ${{{value_id}}} ctic{value_id.capitalize()}, got ${{{value_id}}}`);')
            output_lines.append('')  # Adding a newline for readability

        # Writing to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write('\n'.join(output_lines))

        print(f"Script generated successfully and saved to {output_file_path}")

    except IOError as e:
        print(f"Error opening or reading the file: {e}")


# Example usage
input_file_path = 'input.txt'  # This should be the path to your input file
output_file_path = 'output_script.js'  # The path where you want to save the output script
generate_script(input_file_path, output_file_path)
