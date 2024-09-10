def greet(func):
  def deco(*args, **kwargs):
    print("Good Morning")
    func(*args, **kwargs)
    print("Thanks for using this function")
  return deco

@greet
def hello():
  print("Hello world")

@greet
def add(a, b):
  print(a+b)
  
# greet(hello)()
hello()
# greet(add)(1, 2)
add(1, 2)