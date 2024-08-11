# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, this is a sample file.\n")
    file.write("This file contains some text.")

# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Appending to a file
with open('example.txt', 'a') as file:
    file.write("\nAppending a new line to the file.")
