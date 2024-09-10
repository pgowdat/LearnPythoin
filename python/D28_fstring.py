letter = "Hey my name is {1} and I am from {0}\n"
country = "India"
name = "Harry"
print(letter.format(country, name))


print(f"Hey my name is {name} and I am from {country}")
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}\n")

#place holder:modifier
price = 49.09999
txt = f"For only {price:.2f} dollars!"
print(txt)
# print(txt.format())
print(type(f"{2 * 30}\n"))

#place holder:modifier



x="looked"
print("she %s and %s around\n"%("walked",x))


print(f"He said his age is {(lambda x: x*2)(3)}")
