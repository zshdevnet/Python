class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

    def speak(self, sound):
        return f"{self.name} says {sound}"

dog1 = Dog("Rex")
dog2 = Dog("Luna")

dog1.species = "Wolf"
print(dog1.species)
print(dog2.species)