import csv
from icecream import ic


def read_ids_in_batches(csv_file_path, batch_size):
    """
    Generator function that reads IDs from a CSV file and yields them in batches.

    Parameters:
    - csv_file_path: str, the path to the CSV file.
    - batch_size: int, the number of IDs to yield in each batch.
    """
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        batch = []  # Initialize an empty list to hold the batched data
        for row in csvreader:
            if len(row) > 2:  # Assuming the ID is in the third column
                batch.append(row[2])
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:  # Yield any remaining IDs in the last batch
            yield batch


def write_results(output_file_path, results):
    """
    Writes the processing results to a CSV file.

    Parameters:
    - output_file_path: str, the path to the output CSV file.
    - results: list of tuples, where each tuple contains (ID, 'Pass'/'Fail').
    """
    with open(output_file_path, mode='w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['ID', 'Result'])  # Writing the header
        for result in results:
            csvwriter.writerow(result)




# Processing
from csv_util import read_ids_in_batches, write_results
from icecream import ic


def process_service(id):
    """
    Placeholder function to simulate processing an ID and determining pass/fail.
    Returns a tuple (ID, 'Pass'/'Fail').

    Replace this with the actual service call and error handling.
    """
    # Simulate a service call and error handling
    # For demonstration, randomly pass/fail (replace with actual logic)
    from random import choice
    result = choice(['Pass', 'Fail'])
    return (id, result)


def process():
    input_csv = 'path/to/input.csv'
    output_csv = 'path/to/output.csv'
    batch_size = 100
    all_results = []

    for batch in read_ids_in_batches(input_csv, batch_size):
        ic(batch)
        batch_results = [process_service(id) for id in batch]
        all_results.extend(batch_results)

    write_results(output_csv, all_results)
    ic(f"Processing complete. Results written to {output_csv}")


# Example usage
if __name__ == "__main__":
    process()
