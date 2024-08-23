# a=input("Enter the number: ")
# print(f"Multication table of {a} is: ")

# try:
#     for i in range(1,11):
#         print(f"{a} X {i} = {int(a)*i}")
# except:
#     print("invalid input ")


# print("some imp lines of code ") 
# print("end of program ")   


try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
  print("Index Error")

# handling error to run other lines eg: if data doesnt comes from server