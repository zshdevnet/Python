class BankAccount:
    def __init__(self):
        self.__balance = 0  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def cashup(self,amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance
    
    def __del__(self):
        print("The object is closed!")

acc = BankAccount()

try:
    asking = input("For Deposit input 'D' for cashup input 'C': ")
    
    if asking == ('C' and 'c'):
        acc.cashup(int(input("The amount you want to cashup: ")))
        print(acc.get_balance())
    elif asking == 'D' or asking == 'd':
        acc.deposit(int(input("The amount you want to deposit: ")))
        print(acc.get_balance())
except:
    print("something goes wrong, please try in a moment !")