# def average(a, b, c=1):
#   print("The average is ", (a + b + c) / 2)


def average(*numbers):

  #print("Average is: ", sum / len(numbers))
  #return 7  and parameter as tuple
  print(type(numbers))
  sum = 0
  for i in numbers:
    sum = sum + i

  return sum / len(numbers)


# average(4, 6)
# average(b=9)
# average(b=9,a=20)  order doesn't matter --> key word arguments


c = average(5, 6, 7, 1)
print(c)
print(c.__doc__)


def name(**name): # parameter as dict

  print(type(name))
  print("Hello,", name["fname"], name["mname"], name["lname"]).__doc__


name(mname="Buchanan", lname="Barnes", fname="James").__doc__