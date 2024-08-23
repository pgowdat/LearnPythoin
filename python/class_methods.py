class Employee:
  company = "Apple"
  def show(self):
    print(f"The name is {self.name} and company is {self.company}")

# if we comment @class method , class variable is not updated only instance/object variable updated 
  @classmethod 
  def changeCompany(cls, newCompany):
    cls.company = newCompany
  def changeCompany_1(cls, newCompany):
    cls.company = newCompany


e1 = Employee()
e1.name = "Harry"
e1.show()
print(f"the class variable value is {Employee.company}")
e1.changeCompany("Tesla")
e1.show()
print(f"the class variable value is {Employee.company}")
e1.changeCompany_1("Audi")
e1.show()
print(f"the class variable value is {Employee.company}")