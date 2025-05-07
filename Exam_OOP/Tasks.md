# 🧠 Python Intermediate Exam – OOP (Hard Level)

## ✅ Section 1: Theory Questions

Answer the following:

1. What is the difference between a class and an instance?
2. Explain the purpose of the `__init__` method.
3. What does `self` refer to inside a class?
4. What is inheritance? Give an example use case.
5. What are encapsulation and abstraction? How are they different?

---

## 🧪 Section 2: Code Output

What will this code print?

```python
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
```


## 🔨 Section 3: Coding Tasks – OOP in Python

### ✅ Task 1: Bank Account Class

Create a class `BankAccount` that:

- Has attributes:
  - `account_holder` (str)
  - `balance` (float)
- Has methods:
  - `deposit(amount)` → adds to balance
  - `withdraw(amount)` → subtracts from balance, but returns `"Insufficient funds"` if not enough
  - `__str__()` → returns:  
    `"Holder: [name], Balance: $[balance]"`

---

### ✅ Task 2: Inheritance — Employees

Create:

- A class `Person`:
  - Attributes: `name`, `age`
- A class `Employee` that **inherits** from `Person`:
  - Adds attributes: `employee_id`, `position`
  - Adds a method `introduce()` that prints:  
    `"Hi, I’m [name], [ag] years old, working as [position] (ID: [employee_id])"`

---

### ✅ Task 3 (Optional Bonus): Animal Kingdom — Abstract Classes

Create:

- An abstract class `Animal` (using `ABC`):
  - Has an abstract method: `speak()`
- Two subclasses:
  - `Cat` → implements `speak()` to print `"Meow!"`
  - `Bird` → implements `speak()` to print `"Chirp!"`

Then:

- Create an instance of each class and call their `speak()` methods.

> 💡 Tip: Use this to define abstract base class:
```python
from abc import ABC, abstractmethod
