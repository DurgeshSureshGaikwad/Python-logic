"""in the below example we use a Abstraction, Encapsulation, Inheritance, Polymorphism, Exception Handling and overloading, Constructor, overdraft and other concepts are use in tis example"""

from abc import ABC, abstractmethod

#Abstraction using abstract base class
class Account(ABC):
    def __init__(self,account_number,name,balance):
        self._account_number=account_number  #Encapsulation (Protected)
        self.name=name      #Encapsulation(public)
        self._balance = balance  #Encapsulation (Protected)

    def get_balance(self):
        return self._balance
    
    def _set_balance(self, amount):
        self._balance = amount

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

# Inheritance
class SavingAccount(Account):
    def __init__(self, account_number, name, balance=0):
        super().__init__(account_number, name, balance)

    #Polymorphisam: deffrent behaviour of deposit
    def deposit(self, amount):
        if amount>0:
            self._balance += amount
            print(f"Deposit {amount}. New Balance is: {self._balance}")
        else:
            raise ValueError("Deposit amount must be positive")

    #Polymorphisam: defrent behaviour of withdraw 
    def withdraw(self, amount):
        if amount<=self._balance:
            self._balance -= amount
            print(f"Withdraw {amount}. Remaining Balance is: {self._balance}")
        else:
            raise ValueError("Insufficient Balance.")
        
    def check_balance(self):
        print(f"Available Balance is: {self._balance}")

class CurentAccount(Account):
    def __init__(self, account_number, name, balance=0,overdraft_limit=500):
        super().__init__(account_number, name, balance)
        self.overdraft_limit = overdraft_limit

    #Polymorphisam
    def deposit(self, amount):
        if amount>0:
            self._balance += amount
            print(f"Deposited {amount}. new balance: {self._balance}")
        else:
            raise ValueError("Deposit amount must be Positive")

    #Polymorphisam 
    def withdraw(self, amount):
        if amount<=self._balance + self.overdraft_limit:
            self._balance -= amount
            print(f"Withdraw {amount}. Remaining Balance is: {self._balance}")
        else:
            raise ValueError("Insuficent Balance.")
    
    def check_balance(self):
        print(f"Avilable Balance is: {self.__balance}")

def main():
    try:
        acc1 = SavingAccount("SAV1231","Rajan Vichare",100)
        acc2 = CurentAccount("CUR3442","Vishal Tiuvari",500)

        acc1.deposit(200)
        acc1.withdraw(250)

        acc2.deposit(750)   #Uses overdraft
        acc2.withdraw(970)

        #Polymorpisam in action
        for account in [acc1, acc2]:
            print(f"Account {account._account_number} Balance: {account.get_balance()}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()