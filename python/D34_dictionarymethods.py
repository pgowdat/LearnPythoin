ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

#ep1.update(ep2)
# ep1.clear()
# ep1.pop(122)
ep1.popitem()
del ep1[122]

#del ep1
print(ep1)

#nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)
print(type(myfamily))
print(type(myfamily["child1"]))
x=myfamily.get("child1").get("year")
print(x)

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])
