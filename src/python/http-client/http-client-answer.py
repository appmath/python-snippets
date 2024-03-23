import json
import re
from icecream import ic


# Function to replace environment numbers in URLs
def replace_env_in_url(text, target_env):
    return re.sub(r'(https://url-env)(\d)', r'\g<1>' + target_env, text)


def generate_env_json(input_filename):
    # Read the input file
    with open(input_filename, 'r') as file:
        input_content = file.read()

    # List of environments
    envs = ['env1', 'env2', 'env3', 'env4', 'env5', 'env6', 'env7', 'perf', 'prep']

    # Initialize the dictionary
    data = {}

    # Populate the dictionary, adjusting URLs as necessary
    for env in envs:
        # Determine the environment number (if applicable)
        env_num = re.search(r'\d+', env)
        env_num = env_num.group() if env_num else ''

        # Replace URLs based on the current environment
        adjusted_content = replace_env_in_url(input_content, env_num)

        # Assign the adjusted content to the current environment
        data[env] = adjusted_content

    # Write the dictionary to a JSON file
    with open('http.client.env.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

    ic("JSON file 'http.client.env.json' has been generated.")


def main():
    # Define the name of the input file here
    input_filename = 'input.txt'
    generate_env_json(input_filename)


if __name__ == "__main__":
    main()
