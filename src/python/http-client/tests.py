import re


def generate_code_blocks(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r') as file:
            content = file.read()

        # Regular expression to find the valueIds within the curly braces
        pattern = re.compile(r"const\s*\{([^}]+)\}\s*=\s*body;")
        match = pattern.search(content)

        if not match:
            print("No matching pattern found in the input file.")
            return

        # Extracting valueIds and removing whitespace
        value_ids = [value_id.strip() for value_id in match.group(1).split(',')]

        # Preparing the first code block
        first_block_lines = [
            "> {%",
            'client.test("Request executed successfully", function() {',
            '    client.assert(response.status === 200, `Response is not 200, status: ${response.status}`);',
            '    const body = response.body;\n',
            '    const data = body.data[0];',
            '    const {' + ', '.join(value_ids) + '} = data;\n'
        ]

        # Adding lines to save the values for testing
        for value_id in value_ids:
            first_block_lines.append(f'    client.global.set("{value_id}", {value_id});')

        first_block_lines.extend([
            '',  # Additional newline for spacing
            '});',
            "%}"
        ])

        # Preparing the second code block
        second_block_lines = [
            "> {%",
            'client.test("Request executed successfully", function() {',
            '    client.assert(response.status === 200, `Response is not 200, status: ${response.status}`);',
            '    const body = response.body;\n',
            '    const {' + ', '.join(value_ids) + '} = body;\n'
        ]

        # Adding lines for camelCase variables
        for value_id in value_ids:
            camel_case_id = f'ctic{value_id[0].upper()}{value_id[1:]}'
            second_block_lines.append(f'    const {camel_case_id} = client.global.get("{value_id}");')

        second_block_lines.append('')  # Additional newline for spacing

        # Adding assertion tests with spacing
        for value_id in value_ids:
            camel_case_id = f'ctic{value_id[0].upper()}{value_id[1:]}'
            second_block_lines.append(
                f'    client.assert({value_id} === {camel_case_id}, `Expected ${{{camel_case_id}}} {camel_case_id}, got ${{{value_id}}}`);')

        second_block_lines.extend([
            '',  # Additional newline for spacing
            '});',
            "%}"
        ])

        # Writing to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write('\n'.join(first_block_lines + ['\n'] + second_block_lines))

        print(f"Code blocks generated successfully and saved to {output_file_path}")

    except IOError as e:
        print(f"Error opening or reading the file: {e}")


# Adjusted example usage with the specified file names
input_file_path = 'ctic-values.txt'  # This should be the path to your input file
output_file_path = 'generated-ctic-tests.txt'  # The path where you want to save the output code blocks
generate_code_blocks(input_file_path, output_file_path)
