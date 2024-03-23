import json
import re
from icecream import ic


def replace_env_in_url(text, current_env):
    """
    Replace '-envX' with '-envY' where Y is the target environment number or name.
    """
    return re.sub(r'-env\d+', f'-env{current_env}', text)


def process_input_content(input_content):
    """
    Process the input content to replace environment numbers in URLs
    and organize them into a structured dictionary, except for the "Security" section.
    """
    envs = ['env1', 'env2', 'env3', 'env4', 'env5', 'env6', 'env7', 'perf', 'prep']
    env_structure = {env: {} for env in envs}

    try:
        input_data = json.loads(input_content)

        # Remove the "Security" section and save it for later
        security_data = input_data.pop("Security", None)

        # Process each key-value pair in the input data
        for key, value in input_data.items():
            for env in envs:
                if isinstance(value, str):
                    adjusted_value = replace_env_in_url(value, env.replace('env', ''))
                    env_structure[env][key] = adjusted_value

        # Add the "Security" section back without modification
        if security_data:
            for env in envs:
                env_structure[env]["Security"] = security_data

    except json.JSONDecodeError as e:
        ic('Error parsing input JSON', e)

    return env_structure


def generate_env_json(input_filename, output_filename):
    """
    Generate a JSON file with URLs adjusted for each environment, preserving the "Security" section.
    """
    try:
        with open(input_filename, 'r') as file:
            input_content = file.read()

        # Process the input content to adjust URLs and preserve the "Security" section
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
