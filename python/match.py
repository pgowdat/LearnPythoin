#similar to switch 

x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x>10:
        print(x, "is grater than ten")
   
    case _:
        print(x," else condition")
#no need of break statements like c++