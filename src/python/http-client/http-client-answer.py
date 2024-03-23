import json
import re


def replace_env_in_url(text, target_env):
    """
    Replace the environment number in URLs within the given text.
    """
    return re.sub(r'(https://url-env)(\d)', r'\g<1>' + target_env, text)


def process_input_file(input_filename):
    """
    Read and process the input file, then generate a JSON structure with environment-specific content.
    """
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

    return data


def write_to_json_file(data, output_filename='http.client.env.json'):
    """
    Write the given data to a JSON file.
    """
    with open(output_filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def main(input_filename):
    """
    Main function to orchestrate reading, processing, and writing the environment-specific data.
    """
    # Process the input file to generate the environment-specific data
    data = process_input_file(input_filename)

    # Write the processed data to a JSON file
    write_to_json_file(data)

    # Fun console output
    print("ice cream")


if __name__ == "__main__":
    # Define the name of the input file here
    input_filename = 'input.txt'
    main(input_filename)
