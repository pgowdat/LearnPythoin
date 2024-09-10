# READING A FILE
"""
f = open('myfile.txt', 'r')
# print(f)
text = f.read()
print(text)
f.close()

# WRITING A FILE

# f = open('myfile.txt', 'a')
# f.write('Hello, world!')
# f.close()


# here no need to close the func 

# with open('myfile.txt', 'a') as f:
#   f.write("Hey I am inside with")

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
