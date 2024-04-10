import json


def find_policy_account_number(file_path, line_of_business):
    """
    Finds and prints the pan for the given lineOfBusiness.

    :param file_path: Path to the JSON file.
    :param line_of_business: The lob value to search for.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

            # Assuming 'products' is always present in your JSON structure
            for product in data.get('p-parent', []):
                if product.get('lob') == line_of_business:
                    print(f"Policy Account Number: {product.get('pan')}")
                    break
            else:
                print("No matching lineOfBusiness found.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError:
        print("Error decoding JSON from the file.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    file_path = 'data.json'  # Path to your JSON file
    line_of_business = input("Enter the lineOfBusiness value: ")
    find_policy_account_number(file_path, line_of_business)
