from icecream import ic
import json
import re


def read_and_fix_input(input_filename):
    """
    Attempts to read the input file and wrap its content into a valid JSON string.
    """
    try:
        with open(input_filename, 'r') as file:
            content = file.read().strip()
            fixed_content = "{" + content + "}"
            return fixed_content
    except Exception as e:
        ic('Error reading input file', e)
        return None


def replace_env_in_url(text, env):
    """
    Replace '-envX' with either '-envY' where Y is the target environment number,
    or 'prep' or 'perf' directly if the env is 'prep' or 'perf'.
    """
    new_env = env.replace("env", "")
    if env in ['perf', 'prep']:
        text = re.sub(r'-env\d+', f'-{new_env}', text)
        text = text.replace("71b", "71d")
    else:
        text = re.sub(r'-env\d+', f'-env{new_env}', text)
    return text


def process_input_content(input_content):
    """
    Process the input content to replace environment numbers in URLs
    and organize them into a structured dictionary, except for the "Security" section.
    """
    envs = ['local', 'env1', 'env2', 'env3', 'env4', 'env5', 'env6', 'env7', 'perf', 'prep']
    env_structure = {env: {} for env in envs}

    try:
        input_data = json.loads(input_content)
        security_data = input_data.pop("Security", None)

        # Initialize local with empty strings for URL keys
        url_keys = input_data.keys()
        env_structure['local'] = {key: "" for key in url_keys}

        for env in envs[1:]:  # Skip 'local' since it's already initialized
            for key, value in input_data.items():
                if isinstance(value, str):
                    adjusted_value = replace_env_in_url(value, env)
                    env_structure[env][key] = adjusted_value
            if security_data is not None:
                env_structure[env]["Security"] = security_data

    except json.JSONDecodeError as e:
        ic('Error parsing input JSON', e)

    return env_structure


def generate_env_json(input_filename, output_filename):
    """
    Generate a JSON file with URLs adjusted for each environment, preserving the "Security" section.
    """
    input_content = read_and_fix_input(input_filename)
    if input_content:
        env_data = process_input_content(input_content)

        try:
            with open(output_filename, 'w') as json_file:
                json.dump(env_data, json_file, indent=4)
            ic(f"JSON file '{output_filename}' has been generated.")
        except Exception as e:
            ic('An error occurred while writing the JSON file', e)
    else:
        ic('Failed to process the input file.')


def main():
    input_filename = 'public-env-input.txt'
    output_filename = 'http-client.env.json'
    generate_env_json(input_filename, output_filename)


if __name__ == "__main__":
    main()
