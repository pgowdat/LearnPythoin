class Employee:

  def __init__(self, name):
    self.name = name

  def __len__(self):
    i = 0
    for c in self.name:
      i = i + 1
    return i

  def __str__(self):  #print(str(e)) in main.py
    return f"The name of the employee is {self.name} str"
    
  def __repr__(self):  #print(repr(e)) in main.py
    return f"Employee('{self.name}')"

  def __call__(self):   #(e) in main.py
    print("Hey I am good")