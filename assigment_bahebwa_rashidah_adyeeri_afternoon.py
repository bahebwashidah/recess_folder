import os
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except PermissionError:
        print(f"Permission denied to open file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def write_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
            print(f"Successfully wrote to file '{file_name}'.")
    except PermissionError:
        print(f"Permission denied to write to file '{file_name}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Example usage
file_name = "example.txt"

# Reading file
print("Reading file:")
read_file(file_name)

# Writing to file
print("Writing to file:")
content_to_write = "This is some content to write to the file."
write_file(file_name, content_to_write)

# Reading file again to verify
print("Reading file after writing:")
read_file(file_name)
