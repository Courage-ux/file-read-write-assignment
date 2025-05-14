# file-read-write-assignment

--read_write.py

# Open the original file to read
with open("original.txt", "r") as infile:
    content = infile.read()

# Modify the content (e.g., convert to uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open("modified.txt", "w") as outfile:
    outfile.write(modified_content)

print("File has been modified and saved to 'modified.txt'")

--error_handling.py

# Ask user for a filename
filename = input("Enter the filename to read: ")

try:
    # Try to open the file
    with open(filename, "r") as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You don't have permission to read the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

