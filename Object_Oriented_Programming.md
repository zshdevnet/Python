# OOP - Object Oriented Programming

OOP lets you structure your code like the real world — using classes to define blueprints and objects to represent real entities.

## Classes and Objects
```python
class Car:
    def drive(self):
        print("Car is driving")

my_car = Car()        # Creating an object
my_car.drive()        # Calling method
```

## Constructor and Destructor
```python
class User:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} logged in")

    def __del__(self):
        print(f"{self.name} logged out")

u = User("Shohruz")
```

## Inheritance

```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Woof!")

d = Dog()
d.speak()  # Inherited
d.bark()   # Own method
```

## Polymorphism

```python
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Bark")

def animal_speak(animal):
    animal.speak()

animal_speak(Cat())  # Meow
animal_speak(Dog())  # Bark
```

## Encapsulation
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount()
acc.deposit(100)
print(acc.get_balance())  # 100
```

## Abstraction

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

c = Circle()
print(c.area())
```


## ✅ OOP Summary Table

| **Concept**     | **Purpose**                               | **Keyword / Symbol**       |
|------------------|--------------------------------------------|-----------------------------|
| **Class/Object** | Blueprint and instance                     | `class`, `obj = Class()`    |
| **Constructor**  | Initialize data when object is created     | `__init__()`                |
| **Destructor**   | Cleanup when object is deleted             | `__del__()`                 |
| **Inheritance**  | Reuse parent class features                | `class Child(Parent)`       |
| **Polymorphism** | Same interface, different behavior         | Overriding methods          |
| **Encapsulation**| Hide internal data                         | Prefix with `__var`         |
| **Abstraction**  | Define abstract interface                  | `@abstractmethod`, `ABC`    |
