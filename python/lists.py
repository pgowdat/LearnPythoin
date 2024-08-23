marks = [3, 5, 6, "Pavan", True, 6, 7 , 2, 32, 345, 23]
print(marks)
print(marks[0])
print(marks[1])
print(marks[3])
print(marks[-3])  # len(marks)-3=2 -> marks[2]
print(type(marks))

# print(marks[-3]) # Negative index
# print(marks[len(marks)-3]) # Positive index
# print(marks[5-3]) # Positive index
# print(marks[2]) # Positive index

if "6" in marks:   # 6 is integer not string so else statement
  print("Yes")
else:
  print("No")

# Same thing applies for strings as well!
if "Pa" in "Pavan":
  print("Yes")

print(marks[0:7])
print(marks[1:9])
print(marks[1:9:3])


lst=[i*i for i in range(8)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)