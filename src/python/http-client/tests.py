import re


def generate_code_blocks(input_file_path, output_file_path_1, output_file_path_2):
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
        warning_comment = "// == WARNING: DON'T FORGET TO CONVERT THE VALUES =="

        # Function to check if warning is needed for a specific valueId
        def needs_warning(value_id):
            return value_id in ["userId", "login"]

        # Preparing the first code block
        first_block_lines = [
            "> {%",
            'client.test("Request executed successfully", function() {',
            '    client.assert(response.status === 200, `Response is not 200, status: ${response.status}`);',
            '    const body = response.body;\n',
            '    const data = body.data[0];',
            '    const {' + ', '.join(value_ids) + '} = data;\n'
        ]

        # Adding lines to save the values for testing, with warnings if necessary
        for value_id in value_ids:
            if needs_warning(value_id):
                first_block_lines.append(warning_comment)
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

        # Adding lines for camelCase variables, with warnings if necessary
        for value_id in value_ids:
            camel_case_id = f'ctic{value_id[0].upper()}{value_id[1:]}'
            if needs_warning(value_id):
                second_block_lines.append(warning_comment)
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

        # Writing the first code block to the first output file
        with open(output_file_path_1, 'w') as output_file_1:
            output_file_1.write('\n'.join(first_block_lines))

        # Writing the second code block to the second output file
        with open(output_file_path_2, 'w') as output_file_2:
            output_file_2.write('\n'.join(second_block_lines))

        print(f"Code blocks generated successfully and saved to {output_file_path_1} and {output_file_path_2}")

    except IOError as e:
        print(f"Error opening or reading the file: {e}")


# Adjusted example usage with the specified file names and separate output files
input_file_path = 'ctic-values.txt'
output_file_path_1 = 'generated-ctic-tests-1.txt'
output_file_path_2 = 'generated-ctic-tests-2.txt'
generate_code_blocks(input_file_path, output_file_path_1, output_file_path_2)
