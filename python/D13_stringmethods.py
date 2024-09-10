# strings are immutable
a=" !!!!Pavan!@#!!!!!!!!!"


print(len(a))
print(len(a.center(50)))

print((a.count("!")))

print(a.upper())
print(a.lower())

print(a.strip())
str2 = " Silver Spoon "
print(str2.strip())

print(a.rstrip("!"))
str3 = "Hello !!!"
print(str3.rstrip("!"))

print(a.replace("Pavan","Gowda"))  
print(a.split("@"))  #splits the given string at given instance

blogHeading = "introduction TO JS"
print(blogHeading.capitalize())

str1 = "Welcome to the console !!!"
print(str1.endswith("!!!"))
print(str1.endswith("to",4,10))

str2="He's name is dan. he is an honest"
print(str2)
print(str2.find("is"))
print(str2.find("ish"))
#print(str2.index("ish"))

str3="12345"
print(str3.isalnum())

str4="abcdefg henkdlds" #remove space
print(str4.isalpha()) 


# isalpha will return true if your string consist of A-Z or a-z 0r 0-9
print(str1.isalnum())

print(str2.isalpha())



str5="hello world"
str6="happy ugadi\n"

print(str5.islower())
print(str6.isprintable())
print(str6)


str7="      " #using spacebar
str8="  " #using tabbar
print(str7.isspace())
print(str8.isspace())

str9 = "World Health Organization"
str10 = "World health organization"
print(str9.istitle())
print(str10.istitle())
print(str10.title())


