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

        # Extract URL keys from other environments and set them with empty values for 'local'
        if input_data:
            first_key_set = next(iter(input_data.values()))
            if isinstance(first_key_set, dict):
                for key in first_key_set.keys():
                    env_structure['local'][key] = ""

        for env in envs[1:]:  # Skip 'local' as it's already initialized
            for key, value in input_data.items():
                if isinstance(value, dict):
                    for subkey, subvalue in value.items():
                        if isinstance(subvalue, str):
                            adjusted_value = replace_env_in_url(subvalue, env)
                            env_structure[env][subkey] = adjusted_value
            if security_data is not None:
                env_structure[env]["Security"] = security_data

    except json.JSONDecodeError as e:
        ic('Error parsing input JSON', e)

    return env_structure
