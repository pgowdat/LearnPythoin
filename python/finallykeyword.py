#finally will be useful when we use functions

def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return l[i]
  except:
    print("Some error occurred")
    return str("error!!")

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)
