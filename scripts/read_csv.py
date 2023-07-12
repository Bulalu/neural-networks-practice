import csv

def read_csv(file_path, output_file):
    # Open the CSV file
    with open(file_path, 'r') as file:
        # Initialize a CSV reader
        csv_reader = csv.reader(file)

        # Skip header if it exists
        next(csv_reader, None)

        # Initialize an empty list to store the names
        names = []

        with open(output_file, 'w') as out:

        # Loop through each row in the CSV
            for row in csv_reader:
                # Append the name (second column) to the list
                d = row[1].strip()
                l = d.split(' ')

                first_name = l[0]
                last_name = l[-1]
                out.write(last_name + '\n')
              

    # Return the list of names
    return names

# Usage
file_path = 'data2.csv'
output_files = 'lastname.txt'
read_csv(file_path=file_path, output_file=output_files)