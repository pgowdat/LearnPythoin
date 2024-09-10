name = "Pavan"
friend = " revanth"
anotherFriend = 'Bhuvan'
apple='''HE said "he want to eat apple" '''


print("Hello, "+name)
print("Hello, "+apple)
print(name[0])
print(name[1])
print(name[2])
# print(name[5])

# lets use loop 
for character in apple[0:15:2]:
    print(character,end=" ")
print("\n")
for character in apple:
    print(character,sep=" ",end="")