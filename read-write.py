

# Open the original file to read
with open("original.txt", "r") as infile:
    content = infile.read()

# Modify the content (e.g., convert to uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open("modified.txt", "w") as outfile:
    outfile.write(modified_content)

print("File has been modified and saved to 'modified.txt'")
