class BankAccount:
    def __init__(self,accont_number,init_balance=0):
        self.__account_number=accont_number
        self.__balance=init_balance


    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"deposited {amount}.New balance: {self.__balance}")
        else:
            print("invalid deposite amout ")


    def withdraw(self,amount):
        if 0<amount <=self.__balance:
            self.__balance-=amount
            print(f"wihtdraow {amount}. new balance: {self.__balance}")
        else:
            print("insufficeant funds or invalid withdrawal ")  


    def display(self):
        print(f"account number: {self.__account_number}")
        print(f"Balace : {self.__balance}")


account=BankAccount("2365714879855", 2000)
account.display()

account.deposit(1000)
account.withdraw(300)
account.display()
