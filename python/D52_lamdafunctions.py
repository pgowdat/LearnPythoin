def appl(fx, value):
  return 6 + fx(value)
#Lambda functions are often used in situations where a small function is required for a short period of time.
# They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.
double = lambda x: x * 2
cube = lambda x: x * x * x
avg = lambda x, y, z: (x + y + z) / 3

print(double(5))
print(cube(5))
print(avg(3, 5, 10))
print(appl(lambda x: x * x , 2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
