class Employee:
  def __init__(self, name):
    self.name = name
  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

# class DancerEmployee(Dancer, Employee):
#   def __init__(self, dance, name):
#     self.dance = dance
#     self.name = name

class DancerEmployee(Dancer, Employee):
  def __init__(self, dance, name):
    Dancer.__init__(self, name)
    Employee. __init__(self, name)


    
    

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show() 
print(DancerEmployee.mro())