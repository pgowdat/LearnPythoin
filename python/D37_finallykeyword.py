#finally will be useful when we use functions

def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(f"try-->the index is {i}")
  except:
    print("except-->Some error occurred")

  else:
    x=l[i]
    print(f"else--->the value is {x}")

  finally:
    print("finally-->I am always executed ")
  # print("I am always executed")


func1()

"""
try:
    # Some Code.... 
except:
    # optional block
    # Handling of exception (if required)
else:
    # execute if no exception
finally:
    # Some code .....(always executed)
"""