class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start(self):
        print("Car is starting!")

my_car = Car("Toyota", 2021)

print(my_car.brand)  # Output: Toyota
print(my_car.year)   # Output: 2021