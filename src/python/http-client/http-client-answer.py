import json
import re
from icecream import ic


def replace_env_in_url(text, current_env):
    """
    Replace '-envX' with '-envY' where Y is the target environment number or name.
    """
    if current_env in ['perf', 'prep']:
        target_env = current_env
    else:
        target_env = current_env.replace('env', '')

    return re.sub(r'-env\d+', f'-env{target_env}', text)


def process_input_content(input_content):
    """
    Process the input content to replace environment numbers in URLs
    and organize them into a structured dictionary.
    """
    envs = ['env1', 'env2', 'env3', 'env4', 'env5', 'env6', 'env7', 'perf', 'prep']
    env_structure = {env: {} for env in envs}

    # Split the input content by lines to process each URL entry separately
    lines = input_content.strip().split('\n')
    for line in lines:
        # Attempt to parse each line as JSON to extract the key-value pair
        try:
            line_json = json.loads(f"{{ {line} }}")
            key, value = next(iter(line_json.items()))
            # For each environment, replace the placeholder with the correct environment identifier
            for env in envs:
                adjusted_value = replace_env_in_url(value, env)
                env_structure[env][key] = adjusted_value
        except json.JSONDecodeError as e:
            ic('Error parsing line to JSON', e)
            continue

    return env_structure


def generate_env_json(input_filename, output_filename):
    """
    Generate a JSON file with URLs adjusted for each environment.
    """
    try:
        with open(input_filename, 'r') as file:
            input_content = file.read()

        # Process the input content to adjust URLs
        env_data = process_input_content(input_content)

        # Write the processed data to a JSON file
        with open(output_filename, 'w') as json_file:
            json.dump(env_data, json_file, indent=4)

        ic(f"JSON file '{output_filename}' has been generated.")
    except Exception as e:
        ic('An error occurred', e)


def main():
    input_filename = 'env.txt'
    output_filename = 'http.client.env.json'
    generate_env_json(input_filename, output_filename)


if __name__ == "__main__":
    main()
