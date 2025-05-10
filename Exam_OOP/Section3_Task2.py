class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Employee(Person):

    def __init__(self, name: str, age: int, employee_id: int, position: str):
        # Initialize the parent class (Person)
        super().__init__(name, age)
        self.employee_id = employee_id
        self.position = position

    def introduce(self):
        return f"Hi, I'm {self.name}, {self.age} years old, working as {self.position}, [ID: {self.employee_id}]"
    

# Create an instance of Employee
employee1 = Employee('Shohruz', 22, 1213123, 'Software Developer')
print(employee1.introduce())
