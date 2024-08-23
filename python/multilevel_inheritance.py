class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed
        Animal.__init__(self, name, species="Dog")
        
        
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        self.color = color
        Dog.__init__(self, name, breed="Golden Retriever")
        
        
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o = Dog("tommy", "Husky")
p = GoldenRetriever("jimmy", "brown")
o.show_details()
p.show_details()
print(GoldenRetriever.mro())
