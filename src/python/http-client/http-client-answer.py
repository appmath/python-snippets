import os


def create_folder_structure(parent_folder):
    # Define the folder structure
    folders = [
        os.path.join(parent_folder, "checkout-prod", "env"),
        os.path.join(parent_folder, "checkout-prod", "request-body-input"),
        os.path.join(parent_folder, "test", "env"),
        os.path.join(parent_folder, "test", "request-body-input"),
    ]

    # Create each folder in the structure
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")


if __name__ == "__main__":
    # Ask the user for the parent folder name
    parent_folder = input("Enter the name of the parent folder: ")

    # Create the folder structure
    create_folder_structure(parent_folder)

    print("Folder structure created successfully.")
