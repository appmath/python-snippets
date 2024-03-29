import re


def generate_code_blocks(input_file_path, output_file_path_1, output_file_path_2):
    def needs_warning(value_id):
        """Check if a warning is needed for a specific valueId."""
        return value_id in ["userId", "login"]

    def add_warning_if_needed(value_id, lines):
        """Add a warning comment directly above the code related to 'userId' or 'login'."""
        if needs_warning(value_id):
            lines.append("    // == WARNING: DON'T FORGET TO CONVERT THE VALUES ==")

    def write_code_block(file_path, block_lines):
        """Write the given lines to a file."""
        with open(file_path, 'w') as file:
            file.write('\n'.join(block_lines))
        print(f"Code block written to {file_path}")

    try:
        with open(input_file_path, 'r') as file:
            content = file.read()

        pattern = re.compile(r"const\s*\{([^}]+)\}\s*=\s*body;")
        match = pattern.search(content)

        if not match:
            print("No matching pattern found in the input file.")
            return

        value_ids = [value_id.strip() for value_id in match.group(1).split(',')]
        common_header = [
            "> {%",
            'client.test("Request executed successfully", function() {',
            '    client.assert(response.status === 200, `Response is not 200, status: ${response.status}`);',
            '    const body = response.body;\n'
        ]

        # First block specific lines
        first_block_lines = common_header + [
            '    const data = body.data[0];',
            '    const {' + ', '.join(value_ids) + '} = data;\n'
        ]

        # Adding lines to save the values for testing, with warnings if necessary
        for value_id in value_ids:
            add_warning_if_needed(value_id, first_block_lines)
            first_block_lines.append(f'    client.global.set("{value_id}", {value_id});')

        # Second block specific lines (reuses common_header)
        second_block_lines = common_header.copy() + [
            '    const {' + ', '.join(value_ids) + '} = body;\n'
        ]

        # Adding lines for camelCase variables
        for value_id in value_ids:
            camel_case_id = f'ctic{value_id[0].upper()}{value_id[1:]}'
            add_warning_if_needed(value_id, second_block_lines)
            second_block_lines.append(f'    const {camel_case_id} = client.global.get("{value_id}");')

        # Explicitly adding an empty line for spacing before the tests
        second_block_lines.append('')

        # Adding assertion tests with spacing for the second block
        for value_id in value_ids:
            camel_case_id = f'ctic{value_id[0].upper()}{value_id[1:]}'
            second_block_lines.append(
                f'    client.assert({value_id} === {camel_case_id}, `Expected ${{{camel_case_id}}} {camel_case_id}, got ${{{value_id}}}`);')

        # Common footer for both blocks
        common_footer = ['    });', "%}"]

        # Finalizing both blocks
        first_block_lines.extend(common_footer)
        second_block_lines.extend(common_footer)

        # Writing to files
        write_code_block(output_file_path_1, first_block_lines)
        write_code_block(output_file_path_2, second_block_lines)

    except IOError as e:
        print(f"Error opening or reading the file: {e}")


# Adjusted example usage with the specified file names and separate output files
input_file_path = 'ctic-values.txt'
output_file_path_1 = 'generated-ctic-tests-1.txt'
output_file_path_2 = 'generated-ctic-tests-2.txt'
generate_code_blocks(input_file_path, output_file_path_1, output_file_path_2)
