class Person:

  def __init__(self, name, occ):
    print("Hey I am a person")
    self.name = name
    self.occ = occ

  def info(self):
    print(f"{self.name} is a {self.occ}")


a = Person("Harry", "Developer")
b = Person("Divya", "HR") 
c = Person(1, 2) 
a.info()
b.info()
c.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()