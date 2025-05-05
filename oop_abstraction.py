from abc import ABC, abstractmethod

class Vehicle(ABC):

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def get_vehicle_info(self):
        pass

    @abstractmethod
    def start_engine(self):
        pass

# Define the Car class, which inherits from the abstract base class 'Vehicle'
class Car(Vehicle):
    
    # Constructor method to initialize a Car object
    def __init__(self, make, model, year, car_type, mileage):
        # Call the parent class (Vehicle) constructor to set make, model, and year
        super().__init__(make, model, year)

        # Set a specific attribute for Car: car_type (e.g., SUV, Sedan)
        self.car_type = car_type

        # Private attribute to store mileage (encapsulated — not directly accessible)
        self.__mileage = mileage

    # Implementation of abstract method: returns detailed vehicle info
    def get_vehicle_info(self):
        print(f"{self.make} {self.model}, {self.year} - Type: {self.car_type}")

    # Implementation of abstract method: defines behavior when engine starts
    def start_engine(self):
        print("Car engine started")

    # Public method to access the private mileage attribute (getter)
    def get_mileage(self):
        return self.__mileage

    # Public method to safely update the private mileage attribute (setter)
    def set_mileage(self, new_mileage):
        # Only allow positive values to be set as mileage
        if new_mileage >= 0:
            self.__mileage = new_mileage


car = Car("Hyundai", "Elantra", 2009, "Sedan", 50000)
car.start_engine()
car.get_vehicle_info()
print("Mileage:", car.get_mileage())

car.set_mileage(52000)
print("Updated Mileage:", car.get_mileage())

# This will raise an error:
# print(car.__mileage)  ❌ AttributeError: 'Car' object has no attribute '__mileage'
