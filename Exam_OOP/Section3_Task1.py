class BankAccount:
    account_holder: str = ""
    __balance: float = 0.0

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Insufficient funds")
    
    def withdraw(self, amount: float) -> None:
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient funds")
        
    def __str__(self):
        return f"Account holder: {self.account_holder}, Balance: {self.__balance}"
    

user1 = BankAccount()
user1.account_holder = "John Doe"
user1.deposit(1000)
user1.withdraw(500)
print(user1)

user2 = BankAccount()
user2.account_holder = "Jane Smith"
user2.deposit(2000)
user2.withdraw(200)  # This will raise an error
print(user2)  # Uncommenting this line will raise an error