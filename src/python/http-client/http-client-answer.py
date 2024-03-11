import json
import os


def read_input_file(filename):
    """
    Reads the input file and returns a dictionary of the key-value pairs.
    """
    data = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Properly splitting each line by ': ' to extract key-value pairs
                if ': ' in line:
                    key, value = line.strip().split(': ', 1)
                    data[key.strip('"')] = value.strip('"')
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return None
    return data


def generate_env_data(base_data):
    """
    Generates a dictionary with environments as keys and the base_data as values.
    """
    if base_data is None:
        return None
    env_data = {}
    # Defining the environments
    environments = ['local'] + [f'env{i}' for i in range(1, 8)]
    for env in environments:
        # Copying base_data for each environment
        env_data[env] = base_data.copy()
    return env_data


def write_json_file(data, filename):
    """
    Writes the given data to a JSON file.
    """
    if data is None:
        print("No data to write.")
        return
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def main():
    input_filename = 'input.txt'
    output_filename = 'http.client.private.env.json'

    # Reading the input file
    base_data = read_input_file(input_filename)

    # Generating data for all environments
    env_data = generate_env_data(base_data)

    # Writing the output JSON file
    write_json_file(env_data, output_filename)
    print(f"File '{output_filename}' has been created successfully.")


if __name__ == "__main__":
    main()
