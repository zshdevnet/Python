from abc import ABC, abstractmethod

class SmartDevice(ABC):
    __status = False

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
        self.__status = True
        print(f"Light is now ON")
    
    def turn_off(self):
        self.__status = False
        print(f"Light is now OFF")
    

    def status(self):
        if self.__status == True:
            print("The Smart Light is ON")
        else:
            print("The smart Light is OFF")

class SmartThermostat(SmartDevice):
    def turn_on(self):
        return f"Thermostat is heating up..."
    
    def turn_off(self):
        return f"Thermostat is now OFF"
    
    def status(self):
        return super().status()

statuscheck = SmartLight()
statuscheck.turn_on()
statuscheck.status()
    
