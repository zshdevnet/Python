from abc import ABC, abstractmethod # importing our Abstract Base Class with abstract method decorator

# This is our Interfaace
class User(ABC): # Realising our Class User and inheriting from ABC which makes our class abstract class
    def __init__(self, username): # Initnialising our attributes with the constructor
        self.username = username
        self.__logged_in = False  # private attribute or we can say Encapsulation, we need by default False, it means anyone who open our page he/she not signed in yet to keep close our privite info from rendome visitors.


    @abstractmethod
    def access_dashboard(self): # abstract method access_dashboard, abstract method hiding the implamantation
        pass

    # These two methods we realising for updating our encapsulated data which is Boolean, in other hand we calling it getter/setter
    def login(self): # if the person press on button login, it will call login method and encapsulated data will be updated to the True
        self.__logged_in = True
        print(f"{self.username} logged in.")

    def logout(self): # wiseworse of login
        self.__logged_in = False
        print(f"{self.username} logged out.")

    # this function defines if the user loged in or log out, just returning signal of encapsulated data True or False
    def is_logged_in(self):
        return self.__logged_in


class Admin(User):
    def access_dashboard(self): #implementing our abstract method
        if self.is_logged_in():
            print(f"{self.username} accessing admin panel.")
        else:
            print("Access denied. Please login.")


class Guest(User):
    def access_dashboard(self): #implementing our abstract method
        print("Guest users can only view public content.")