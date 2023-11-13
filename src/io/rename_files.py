import os


def add_a_to_filenames(folder_path):
    # Check if the provided path is a directory
    if not os.path.isdir(folder_path):
        print("The provided path is not a directory.")
        return

    # Iterate over all files in the directory
    for filename in os.listdir(folder_path):
        old_file = os.path.join(folder_path, filename)

        # Check if it's a file and not a directory
        if os.path.isfile(old_file):
            new_filename = 'A' + filename
            new_file = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed {filename} to {new_filename}")


# Replace 'your_directory_path' with the path to the directory containing the files you want to rename
add_a_to_filenames('your_directory_path')
