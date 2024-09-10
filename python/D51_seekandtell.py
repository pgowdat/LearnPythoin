# if you want to truncate the file to a specific size, you can use the truncate function.
with open('sample.txt', 'w') as f:
  f.write('Hello World3!')
  f.truncate(5)


with open('sample.txt', 'r') as f:
  print(f.read())

#The seek() function allows you to move the current position within a file to a specific point.
with open('myfile.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)
  # Read the next 5 bytes
  data = f.read(5)
  print(data)

#The tell() function returns the current position within the file, in bytes.
with open('myfile.txt', 'r') as f:
  # Read the first 5 bytes
  data = f.read(5)
  print(data)
  # Save the current position
  current_position = f.tell()
  # Seek to the saved position
  f.seek(current_position)
  print(current_position)
  print(f.read(5))