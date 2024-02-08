import csv

import csv


def read_third_column(csv_file_path):
    """
    Reads the third column from a CSV file.

    Parameters:
    - csv_file_path: str, the path to the CSV file.
    """
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)

        # Iterate over each row in the CSV
        for row in csvreader:
            # Ensure the row has at least three columns
            if len(row) > 2:
                third_column_value = row[2]
                print(third_column_value)


# Example usage
csv_file_path = 'path/to/your/file.csv'
read_third_column(csv_file_path)
