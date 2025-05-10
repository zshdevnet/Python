from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Cat(Animal):

    def speak(self):
        print('Meow!')

class Bird(Animal):

    def speak(self):
        print("Chirp!")

cat1 = Cat()
cat1.speak()

bird1 = Bird()
bird1.speak()