import os
"""
if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}") """

# Open the file in read-only mode
f = os.open("myfile.txt", os.O_RDONLY)
# Read the contents of the file
contents = os.read(f, 1024)
# Close the file
print(contents)
os.close(f)

# Open the file in write-only mode
f = os.open("myfile.txt", os.O_WRONLY)
# Write to the file
os.write(f, b"Hello, world!")
# Close the file
os.close(f)

#interacting with file
# Get a list of the files in the current directory
files = os.listdir(".")
print(files)  # Output: ['myfile.txt', 'otherfile.txt']


#running system commands
# Run the "ls" command and print the output
output = os.system("ls")
print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# Run the "ls" command and get the output as a file-like object
f = os.popen("ls")
# Read the contents of the output
output = f.read()
print(output)  # Output: ['myfile.txt', 'otherfile.txt']
# Close the file-like object
f.close()
"""
# Replace "YourUsername" with your actual system username
file_path = "C:/Users/Pavan/Downloads/file.txt" # Windows
# file_path = "/Users/YourUsername/Downloads/yourfile.txt"  # macOS/Linux

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")

# Replace "YourUsername" with your actual system username
file_path = "C:/Users/Pavan/Downloads/file.txt" # Windows
# file_path = "/Users/YourUsername/Downloads/yourfile.txt"  # macOS/Linux

try:
    # Opening the file in write mode ('w')
    with open(file_path, 'w') as file:
        file.write("This is the content being written to the file.\n")
        print(f"Content written to {file_path}")
except FileNotFoundError:
    print(f"The file at {file_path} could not be opened.")
"""