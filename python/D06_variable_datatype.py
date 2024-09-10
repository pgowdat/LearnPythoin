''' the practise
    multi line comments '''
print("Pavan Gowda ")
print("king")
print("Hi","i am",1,"the pavan",sep="----",end=" gowda\n")
a=11
b=True
c="pavan"
d='a'
e=complex(8,2)
print(e)
print("type of a is ",type(a))
print("type of b is ",type(b))
print("type of c is ",type(c))
print("type of d is ",type(d))

#In python everything is considered object like integer,bool,lists,dictionary, tuple

list1=[2,3.6,[4,9],["apple","banana"]]
print(list1)

tuple1=(1,3.5,("parrot","sparrow"),(2,4))
print(tuple1)


dict1={"name":"Pavan","age":22,"can vote":True}
print(dict1)

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

string_letters = str(letters)
lists_letters = list(letters)
tuples_letters = tuple(letters)
sets_letters = set(letters)

#ordered
print("String: ", string_letters)
print() # for new line
print("Lists: ", lists_letters)
print() # for new line
print("Tuples: ", tuples_letters)

#unordered
print() # for new line
print("Sets: ", sets_letters)