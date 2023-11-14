import os
import re


def rename_java_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".java"):
            # Construct new file name
            new_filename = 'A' + filename
            new_file_path = os.path.join(folder_path, new_filename)
            old_file_path = os.path.join(folder_path, filename)

            # Read the old file
            with open(old_file_path, 'r') as file:
                filedata = file.read()

            # Find the class name and replace it
            # Assuming the file name (without .java) is the class name
            class_name = filename[:-5]
            new_class_name = 'A' + class_name
            filedata = re.sub(r'\b' + class_name + r'\b', new_class_name, filedata)

            # Write the changes to the new file
            with open(new_file_path, 'w') as file:
                file.write(filedata)

            # Remove the old file
            os.remove(old_file_path)

            print(f"Renamed {filename} to {new_filename} and updated class name to {new_class_name}")


folder_path = '/path/to/your/folder'  # Replace with your folder path
rename_java_files(folder_path)
