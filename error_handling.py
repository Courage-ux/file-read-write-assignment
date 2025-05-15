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
