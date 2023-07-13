def remove_empty_lines(file_path):
    # Open the file and read the lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove empty lines
    lines = [line.lower() for line in lines if line.strip() != '']

    # Write the modified lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)

# Usage
file_path = 'lastname.txt'
remove_empty_lines(file_path)