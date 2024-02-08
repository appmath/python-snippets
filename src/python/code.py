import csv

# Path to your CSV file
csv_file_path = 'path/to/your/file.csv'

# Open the CSV file
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)

    # Iterate over each row in the CSV
    for row in csvreader:
        # Access and print the third column of each row
        # Check if the row has enough columns to avoid IndexError
        if len(row) > 2:
            third_column_value = row[2]
            print(third_column_value)
