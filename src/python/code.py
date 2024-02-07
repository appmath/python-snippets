from configparser import ConfigParser


def get_config_value(filename='credentials.ini', section='default', key=None):
    """
    Fetches a single value or all values from a specified section in the INI file.

    :param filename: The INI file to read from.
    :param section: The section within the INI file.
    :param key: The specific key to fetch from the section. If None, all key-value pairs are returned.
    :return: A single value if key is specified, or a dictionary of key-value pairs if key is None.
    """
    parser = ConfigParser()
    parser.read(filename)

    # Check if the section exists
    if parser.has_section(section):
        if key:
            # Return the specific value for the key if it exists
            if parser.has_option(section, key):
                return parser.get(section, key)
            else:
                raise KeyError(f'Key {key} not found in section {section}')
        else:
            # Return all key-value pairs in the section
            return {item[0]: item[1] for item in parser.items(section)}
    else:
        raise Exception(f'Section {section} not found in the {filename}')


# Usage examples:

# Fetching a specific key (e.g., Okta password)
okta_password = get_config_value(section='okta', key='API_OKTA_PASSWORD')
print(okta_password)

# Fetching all credentials from a section
credentials = get_config_value(section='credentials')
print(credentials)
