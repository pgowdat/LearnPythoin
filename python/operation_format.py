print(5+6)
print(5-6)
print(5*6)
print(5%6)
print(5**3)
print(15/6)
print(15//6)


import random

print(random.randrange(1, 10))

text=" pavan is good boy "

if "pavan" in text:
   print("yes")
print(text[0:4])   
print(text[-7:-1])   
print(text[2:])   
print(text[:5]) 
print(text.replace("p","r")) 
print(text.upper()) #The upper() method returns the string in upper case:
print(text.strip()) #The strip() method removes any whitespace from the beginning or the end:

a="KING pavan"
print(a.replace("p","r"))


b = "Hello, World!"
print(b.split(",")) # returns ['Hello', ' World!']

#The format() method takes the passed arguments, formats them,
# and places them in the string where the placeholders {}
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

myorder = "I want to pay {} dollars for {} pieces of item {}."
print(myorder.format(quantity, itemno, price))

num=1
txt="pavan is {}"
print(txt.format(num))