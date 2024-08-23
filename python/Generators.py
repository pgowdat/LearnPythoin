"""Generators in Python are special type of functions that allow you to create an iterable sequence
of values. A generator function returns a generator object, which can be used to generate the 
values one-by-one as you iterate over it"""


def my_generator():
    for i in range(0,500,5):
      # Complex computations
      yield i

gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in  gen:
  print(j)