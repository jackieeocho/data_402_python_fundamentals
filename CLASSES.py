class Dog:

    animal_kind = "canine"

    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def bark(self): #first parameter is called self because it refers back to itself?
        return"woof"

spot = Dog("Spot","red") #this is the object 'spot'
print(spot.name)
print(spot.animal_kind)
luna = Dog("Luna","Grey")

class Employees:

    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname

id_1 = Employees("Jane", "Doe")
id_2 = Employees("Dane", "Joe")

print(id_2.surname)

