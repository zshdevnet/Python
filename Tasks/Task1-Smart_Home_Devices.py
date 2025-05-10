from abc import ABC, abstractmethod

class SmartDevice(ABC):
    
    def __init__(self):
        self._status = False  # Use single underscore to allow subclass access

    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def status(self):
        pass


class SmartLight(SmartDevice):

    def turn_on(self):
        self._status = True
        print(f"Light is now ON")
    
    def turn_off(self):
        self._status = False
        print(f"Light is now OFF")
    

    def status(self):
        if self._status:
            print("The Smart Light is ON")
        else:
            print("The Smart Light is OFF")


class SmartThermostat(SmartDevice):
    
    def turn_on(self):
        self._status = True
        print(f"Thermostat is heating up...")
    
    def turn_off(self):
        self._status = False
        print(f"Thermostat is now OFF")
    
    def status(self):
        if self._status:
            print("The Smart Thermostat is ON")
        else:
            print("The Smart Thermostat is OFF")


# 🔄 **Testing the objects**
obj1 = SmartLight()
obj1.turn_on()
obj1.status()  # Output: The Smart Light is ON

print("\n")  # Separator

obj2 = SmartThermostat()
obj2.turn_off()
obj2.status()  # Output: The Smart Thermostat is OFF
