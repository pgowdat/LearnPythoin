f = open('myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
#The readlines() method reads all the lines of the file and returns them as a list of strings.

f = open('myfile.txt', 'w')
lines1 = ['line 1\n', 'line 2\n', 'line 3\n']
lines2=("hi hello"," namaskara")
f.writelines(lines1)
f.writelines(lines2)
f.close()
#The writelines() method in Python writes a sequence of strings to a file.
# The sequence can be any iterable object, such as a list or a tuple.

f = open('myfile.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()